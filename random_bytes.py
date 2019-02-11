import time
import os
import base64
import random
import numpy
from flask import Flask
from flask import Response


app = Flask(__name__)

BYTE_SIZE = 256

def random():
    while True:
        time.sleep(1)
        block = random_block("SELCUK", "KARAKAYALI")
        f = ""
        for elem in zip(block[0].split(os.linesep),
                        block[1].split(os.linesep)):
            f += (f"{elem[0]}{elem[1]: >20}\n")
        yield(
            f'''--bytes\r\n
            Content-Disposition: x-www-form-urlencoded\r\n\r\n
            {f}
            \r\n''')


@app.route("/")
def hello_world():
    return Response(random(), mimetype='multipart/form-data; boundary=bytes')


# TODO make this a generator
# TODO include offset so (offset) (16 bytes) (ascii)
# TODO use numparray instead of tuple
def random_block(name):
    bytez = bytearray(os.urandom(BYTE_SIZE))

    start, end = (random.randint(0, BYTE_SIZE - len(name)), len(name))

    bytez[start:end] = name.encode('ascii')

    np_arr = np.array(bytez).reshape(BYTE_SIZE / 16, 16)

    hex_chars = base64.b16encode(bytez).decode()

    hex_block = ""

    for r in range(0, len(b16), 32):
        for c in range(0, 32, 2):
            i = r + c
            hex_block += hex_chars[i:i+2] + " "
        hex_block += os.linesep
    print(hex_block)
    ascii_block = ""

    ascii = bytez.decode('ascii', 'replace').replace('\ufffD', '.')
    string = ''.join([c if c.isprintable() else '.' for c in ascii])
    for i in range(0, BYTE_SIZE, 16):
        ascii_block += string[i:i+16] + os.linesep

    yield (ascii_block)


for n in random_block("SELCUK KARAKAYALI"):
    print(n)
