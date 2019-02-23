import time
import os
import base64
import random
import numpy


def random_hex(text=None, length=256):
    """
    rows of 16 bytes
    """
    bytez = bytearray(os.urandom(length))
    start = random.randint(0, length - len(text))
    end = start + len(text)
    bytez[start:end] = text.encode('ascii')
    yield (numpy.array(bytez).reshape(length // 16, 16))


def bytes_to_ascii(bytez, replace='.'):
    """
    Converts bytes type given into printable
    ascii characters
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


if __name__ == '__main__':
    while True:
        r = random_hex("SELCUK KARAKAYALI")
        time.sleep(0.5)
        print(hex_dump(next(r)), end='')
