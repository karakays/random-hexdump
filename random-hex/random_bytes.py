import time
import os
import random
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=('INFO'))

SIZE = 256
CHUNK_SIZE = 16


def coroutine(func):
    def start(*args,**kwargs):
        g = func(*args,**kwargs)
        g.__next__()
        return g
    return start


def char_encode(bytez, replace='.'):
    """
    Encodes bytes given into ascii characters
    while non-printable characters are replaced
    with <p>replace</p>
    """
    chars = bytez.decode('ascii', 'replace').replace('\ufffD', replace)
    return ''.join([c if c.isprintable() else '.' for c in chars])


def random_chunk(size=SIZE):
    iterate = size // CHUNK_SIZE
    while iterate:
        yield os.urandom(CHUNK_SIZE)
        iterate -= 1


def dump_chunk():
    offset = 0x00
    @coroutine
    def next():
        nonlocal offset
        chunk = None
        for bytez in random_chunk():
            loc = yield(chunk)
            logger.debug("received=%s", loc)

            if loc:
                ind, txt = loc
                bytez_array = bytearray(bytez)
                bytez_array[ind:ind + len(txt)] = txt.encode('ascii')
                bytez = bytes(bytez_array)

            hex_col = " ".join([f"{b:02X}" for b in bytez])
            ascii_col = char_encode(bytes(bytez))
            chunk = f"{offset:08X} {hex_col} {ascii_col}"
            offset += CHUNK_SIZE
    return next


def dump_block(size=256, text=None):
    next_chunk = dump_chunk()()
    txt_locs = find_txt_locs(text)
    logger.debug("Got locs=%s", txt_locs)
    offset = 0x00

    try:
        while True:
            loc = txt_locs.get(offset)
            chunk = next_chunk.send(loc)
            yield(chunk)
            time.sleep(0.5)
            offset += CHUNK_SIZE
    except StopIteration:
            logger.debug("Done consuming")


def find_txt_locs(text):
    curr_ind = random.randint(0, SIZE - len(text))

    txt_ind = 0
    txt_os = (curr_ind // CHUNK_SIZE) * CHUNK_SIZE
    locs = {}

    while txt_ind < len(text):
        logger.debug("curr_ind=%s, txt_ind=%s, txt_os=%s",
                    curr_ind, txt_ind, txt_os)
        rel_ind = curr_ind % CHUNK_SIZE
        logger.debug("rel_ind=%s", rel_ind)
        txt_end = txt_ind + CHUNK_SIZE - rel_ind
        chunk_txt = text[txt_ind:txt_end]
        logger.debug("chunk_txt=%s", chunk_txt)
        locs[txt_os] = (rel_ind, chunk_txt)
        curr_ind += len(chunk_txt)
        txt_ind += len(chunk_txt)
        txt_os += CHUNK_SIZE

    return locs


if __name__ == '__main__':
    for line in dump_block(text = "selcuk karakayali"):
        print(f"{line}")
