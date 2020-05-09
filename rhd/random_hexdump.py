import time
import os
import random
import logging
import sys


logger = logging.getLogger(__name__)
logging.basicConfig(level=('INFO'))

BLOCK_SIZE = 0x100
CHUNK_SIZE = 0x10
global_offset = 0x00


def coroutine(func):
    def start(*args,**kwargs):
        g = func(*args,**kwargs)
        g.__next__()
        return g
    return start


def printable_encode(bytez, replace='.'):
    """
    Encodes bytes given into ascii characters
    while non-printable characters are replaced
    with <p>replace</p>
    """
    chars = bytez.decode('ascii', 'replace').replace('\ufffD', replace)
    return ''.join([c if c.isprintable() else '.' for c in chars])


class TextOffset:
    def __init__(self, block_offset, text, chunk_index):
        self.block_offset = block_offset
        self.text = text
        self.chunk_index = chunk_index


def find_text_offset(text, block_index):
    text_index = 0
    locs = {}
    text_block_offset = (block_index // CHUNK_SIZE) * CHUNK_SIZE
    logger.debug("Found text_index=%s and text_offset=%s inside block",
                 block_index, text_block_offset)

    while text_index < len(text):
        #logger.debug("curr_ind=%s, txt_ind=%s, txt_os=%s",
        #            text_block_index, text_index, text_block_offset)
        start_index_in_chunk = block_index % CHUNK_SIZE
        end_index_in_chunk = text_index + CHUNK_SIZE - start_index_in_chunk
        chunk_txt = text[text_index:end_index_in_chunk]
        logger.debug("Allocating text=%s starting at=%s, ending at=%s relatively",
                    chunk_txt, start_index_in_chunk, end_index_in_chunk)
        locs[text_block_offset] = (start_index_in_chunk, chunk_txt)
        block_index += len(chunk_txt)
        text_index += len(chunk_txt)
        text_block_offset += CHUNK_SIZE
        #logger.debug("block_index=%s, txt_ind=%s, txt_os=%s",
        #            text_block_index, text_index, text_block_offset)

    return locs


def swap_bytes(bytez, start_index, new_bytez):
    """
    Swap bytes in <p>bytez<p> from ascii encoded
    ascii_text starting from index, inclusive
    return immutable bytes
    """
    bytez_array = bytearray(bytez)
    end_index = start_index + len(new_bytez)
    bytez_array[start_index:end_index] = new_bytez
    return bytes(bytez_array)


def random_chunk():
    while True:
        yield os.urandom(CHUNK_SIZE)


def render_hex(chunk, start_index, end_index):
    bytes_hex = " ".join([f"{b:02X}" for b in chunk])
    mark_start = (start_index * 2) + start_index
    mark_end = (end_index * 2) + end_index - 1
    marked = bytes_hex[mark_start:mark_end]
    logger.debug("hex=%s, hex_mark=%s", bytes_hex, marked)
    if end_index:
        bytes_hex = bytes_hex.replace(marked, f"\033[1;32;40m{marked}\033[0m")
    return bytes_hex


def render_ascii(chunk, start_index, end_index):
    bytes_ascii = printable_encode(bytes(chunk))
    marked = bytes_ascii[start_index:end_index]
    return bytes_ascii.replace(marked, f"\033[1;32;40m{marked}\033[0m") if marked else bytes_ascii


def dump_line():
    @coroutine
    def next():
        global global_offset
        line = None
        for chunk in random_chunk():
            loc = yield(line)
            logger.debug("Yield line received location=%s", loc)
            index, text = loc
            swapped_bytes = swap_bytes(chunk, index, text.encode())
            hexed = render_hex(swapped_bytes, index, index + len(text))
            asciied = render_ascii(swapped_bytes, index, index + len(text))
            line = f"{global_offset:X} {hexed} {asciied}"
            global_offset += CHUNK_SIZE
        # Yield the last chunk here. since this co-routine stays one-step
        # behind the random_chunk generator, this is necessary to prevent
        # last chunk to be lost.
        yield(line)
    return next


def dump_block(text):
    offset = 0
    next_line  = dump_line()()
    text_offsets = dict()
    if text:
        text_block_index = random.randint(0, BLOCK_SIZE - len(text))
        text_offsets = find_text_offset(text, text_block_index)
    logger.debug("Received text_offset=%s", text_offsets)

    try:
        while offset < BLOCK_SIZE:
            loc = text_offsets.get(offset, (0, ''))
            chunk = next_line.send(loc)
            yield(chunk)
            offset += CHUNK_SIZE
    except StopIteration:
            logger.debug("Done with dumping block at offset=%s...", offset)


def run(txt = None):
    global global_offset
    global_offset = int.from_bytes(os.urandom(8), byteorder='little')
    while True:
        for line in dump_block(text=txt):
            print(f"{line}")
            time.sleep(0.1)
