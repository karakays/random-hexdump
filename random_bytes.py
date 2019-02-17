import time
import os
import base64
import random
import numpy


def random_hex(name=None, length=256):
    """
    rows of 16 bytes
    """
    bytez = bytearray(os.urandom(length))
    start = random.randint(0, length - len(name))
    end = start + len(name)
    bytez[start:end] = name.encode('ascii')
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
    hex_dmp = ""
    os = offset

    for e in byte_np:
        hr = " ".join([f"{b:02X}" for b in e])
        ar = bytes_to_ascii(bytes(e))
        hex_dmp += f"{os:08X} {hr} {ar}\n"
        os += 16

    return hex_dmp


if __name__ == '__main__':
    for n in random_hex("SELCUK KARAKAYALI"):
        time.sleep(2)
        print(hex_dump(n))
