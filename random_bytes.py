import time
import os
import base64
import random
import numpy


def random_hex(name=None, byte_len=256):
    bytez = bytearray(os.urandom(byte_len))
    start = random.randint(0, byte_len - len(name))
    end = start + len(name)
    bytez[start:end] = name.encode('ascii')
    yield (numpy.array(bytez).reshape(byte_len // 16, 16))


def to_ascii(bytez):
    pass


def hex_dump(byte_arr, offset=None):
    hex_chars = base64.b16encode(bytez).decode()

    hex_block = ""

    for r in range(0, len(b16), 32):
        for c in range(0, 32, 2):
            i = r + c
            hex_block += hex_chars[i:i+2] + " "
        hex_block += os.linesep
    ascii_block = ""

    ascii = bytez.decode('ascii', 'replace').replace('\ufffD', '.')
    string = ''.join([c if c.isprintable() else '.' for c in ascii])
    for i in range(0, BYTE_SIZE, 16):
        ascii_block += string[i:i+16] + os.linesep

    yield (ascii_block)


if __name__ == '__main__':
    for n in random_hex("SELCUK KARAKAYALI"):
        time.sleep(2)
        print(n)
