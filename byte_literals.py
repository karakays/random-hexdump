#!/usr/bin/env python3

# bytes built-in type is represented as ascii text in its output

# byte literals prefix with b
byte = b'\x16'
print(f'value: {byte}')

# byte literals are resolved into bytes built-in type
print(f'type: type={byte}')

# 0x61 matches ASCII 'a' character
byte = b'\x61'
print(byte)

# '97' is not integer 97 value, its ASCII encoded value
byte = b'97'
print(f'representation: {byte}, binary value: {byte.hex()}')

# bytes implements sequence and each element is a byte 0<=b<=255
b = b'abc'
# prints int value
print(f"b[1]={b[1]}")


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

# encode as hex
b = bytes((10, 11, 12))
