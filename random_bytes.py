import time
import os
import base64
from flask import Flask
from flask import Response


app = Flask(__name__)


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


def random_block(first_name, last_name):
    BYTE_SIZE = 256

    bytez = bytearray(os.urandom(BYTE_SIZE))

    bytez[70:len(first_name)] = first_name.encode('ascii')
    bytez[86:len(last_name)] = last_name.encode('ascii')

    b16 = base64.b16encode(bytez).decode()

    hex_block = ""

    for r in range(0, len(b16), 32):
        for c in range(0, 32, 2):
            i = r + c
            hex_block += b16[i:i+2] + " "
        hex_block += os.linesep

    ascii_block = ""

    ascii = bytez.decode('ascii', 'replace').replace('\ufffD', '.')
    string = ''.join([c if c.isprintable() else '.' for c in ascii])
    for i in range(0, BYTE_SIZE, 16):
        ascii_block += string[i:i+16] + os.linesep

    return (hex_block, ascii_block)


result = random_block("SELCUK", "KARAKAYALI")


for elem in zip(result[0].split(os.linesep), result[1].split(os.linesep)):
    print(f"{elem[0]}{elem[1]: >20}")
