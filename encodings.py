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


s = "hello"
print(f"string to binary b={s.encode()}, type: type(s.encode())") # utf-8 character encoding by default
print(f"b={s.encode('ascii')}, type: type(s.encode('ascii'))")
print(f"b={s.encode('utf-8')}, type: type(s.encode('utf-8'))")


b16 = base64.b16encode(b)
print(f"b16={b16}, type={type(b16)} len={len(b16)}")

b64 = base64.b64encode(b)
print(f"b64: {b64}, type={type(b64)}, len: {len(b64)}")

test = b'DEAD'
print(f"""test.decode(): {test.decode()},"""
      f"""type(test.decode()): {type(test.decode())}""")

# bytes vs text conversions...

# to convert bytes to txt
# bytes.decode()
b = b'\x61\x62\x63'
s = b.decode()
print(f's={s}, type={type(s)}')

# to convert str to bytes
# str.encode()
s = 'abc'
b = s.encode()
print(f'b={b}, type={type(b)}')

