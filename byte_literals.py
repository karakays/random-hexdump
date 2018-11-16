#!/usr/bin/env python3

# byte literals prefix with b
byte = b'\x16'
print(f'type: {type({byte})}, value: {byte}')

# 0x61 matches ASCII 'a' character
byte = b'\x61'
print(byte)

# '97' is not integer 97 value, its ASCII encoded value
byte = b'97'
print(f'representation: {byte}, binary value: {byte.hex()}')

# If it does not correspond to ASCII char, then hex value represented.
a = b'\x128'
b = b'\x01'
print(f'{a}, {b}')

# return 5 empty bytes
b = bytes(5)
print(b)

# convert ints to bytes
b = bytes([12, 255, 44])
print(b)

# string representation is ascii encoded text
b = b'abcd'
print('%s, %s' % (b[0], b[3]))

# factory class method from hex encoded data
print(bytes.fromhex('FF01'))
# whitespaces ignored
print(bytes.fromhex('FF 01 AA    BB   '))
