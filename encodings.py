#!/usr/bin/env python3

import os
import random
import base64

b = random.getrandbits(16 * 8)
print(b)

b = os.urandom(16)
print(f"hexify: {b.hex()}, type: str={type(b.hex())}")

for i in b:
    print(f"{i:02X}", end="")
print()

b16 = base64.b16encode(b)
print(f"b16={b16}, type={type(b16)} len={len(b16)}")

b64 = base64.b64encode(b)
print(f"b64: {b64}, type={type(b64)}, len: {len(b64)}")

test = b'DEAD'
print(f"""test.decode(): {test.decode()},"""
      f"""type(test.decode()): {type(test.decode())}""")

BYTE_SIZE = 512

b = bytearray(os.urandom(BYTE_SIZE))
print(f"len of bytearray {len(b)}")
print(b.hex())

b[70:76] = b'SELCUK'
b[86:96] = b'KARAKAYALI'

print(f"len of bytearray {len(b)}")
b16 = base64.b16encode(b)
print(f"len of bytearray {len(b16)}")
print(f"b16-type: {type(b16)}, len: {len(b16)}")
print(b16)

b16 = bytearray(b16)
b16 = b16.decode(encoding='ascii')
print(f"b16-type: {type(b16)}, len: {len(b16)}")
print(b16)

for r in range(0, len(b16), 32):
    for c in range(0, 32, 2):
        i = r + c
        octet = b16[i:i+2]
        print(f"{octet} ", end="")
    print()

ascii = b.decode('ascii', 'replace').replace('\ufffD', '.')
string = ''.join([c if c.isprintable() else '.' for c in ascii])
print(f'str_len: {len(string)}')
for i in range(0, BYTE_SIZE, 16):
    print(string[i:i+16])
