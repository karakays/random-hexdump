import logging
import time
import os
import base64
import random
import numpy


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
    Encodes bytes given to ascii characters.
    Non-printable ascii characters are replaced
    with <p>replace</p>
    """
    chars = bytez.decode('ascii', 'replace').replace('\ufffD', replace)
    return ''.join([c if c.isprintable() else '.' for c in chars])


def random_hex_np(text=None, length=256):
    """
    rows of 16 bytes
    """
    bytez = bytearray(os.urandom(length))
    start = random.randint(0, length - len(text))
    end = start + len(text)
    bytez[start:end] = text.encode('ascii')
    yield (numpy.array(bytez).reshape(length // 16, 16))


def random_block(size, iterate=100):
    while iterate:
        yield os.urandom(size)
        iterate -= 1


def dump_block(size=0x10, offset=0x00):
    def next():
        nonlocal offset
        chunk = None
        for bytez in random_block(size):
            text = yield(chunk)
            print(f"text is {text}")
            hex_col = " ".join([f"{b:02X}" for b in bytez])
            ascii_col = char_encode(bytes(bytez))
            chunk = f"{offset:08X} {hex_col} {ascii_col}"
            #yield chunk
            #print(f"chunk in here is 2{chunk}")
            offset += size
    return next


def dump(size=256, text=None):
    #beg_ind = random.randint(0, size - len(text))
    #end_ind = start + len(text)

    next_line = dump_block(size // CHUNK_SIZE, 0)
    offset = 0x00

    coroutine = next_line()
    coroutine.__next__()
    ### start
    #coroutine.send(None)
    for chunk in coroutine:
        print(f"dump: {chunk}")
        coroutine.send("abc")
        time.sleep(0.5)
        offset += CHUNK_SIZE


def char_encode(bytez, replace='.'):
    """
    Encodes bytes given to ascii characters.
    Non-printable ascii characters are replaced
    with <p>replace</p>
    """
    chars = bytez.decode('ascii', 'replace').replace('\ufffD', replace)
    return ''.join([c if c.isprintable() else '.' for c in chars])


def hex_dump(byte_np, offset=0):
    """
    Returns hexadecimal representation of the
    numpy array of bytes given
    """
    row = None
    line = None
    word = "2 bytes"
    output = ""

    for e in byte_np:
        hex_col = " ".join([f"{b:02X}" for b in e])
        ascii_col = bytes_to_ascii(bytes(e))
        output += f"{offset:08X} {hex_col} {ascii_col}\n"
        offset += 16

    return output

x = -1

def foo():
    nonlocal x
    while True:
        y = yield(x)
        x += 1


if __name__ == '__main__':
    g = foo()
    for e in g:
        print(e)
        time.sleep(1)
