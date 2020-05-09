from rhd import random_hexdump


def test_render_non_printable_encode():
    chunk = b'\x0ABCDEF'
    asciied = random_hexdump.render_ascii(chunk, 0, 0)
    assert asciied == '.BCDEF'


def test_printable_encode():
    chunk = b'\x0ABCDEF'
    asciied = random_hexdump.render_ascii(chunk, 0, 0)
    assert asciied == '.BCDEF'


def test_swap_empty_bytes():
    chunk = b'ABCDEF'
    swapped = random_hexdump.swap_bytes(chunk, 0, b'')
    assert swapped == chunk


def test_swap_bytes():
    chunk = b'ABCDEF'
    swapped = random_hexdump.swap_bytes(chunk, 0, b'000')
    assert swapped == b'000DEF'


def test_random_chunk():
    chunk = random_hexdump.random_chunk()
    assert next(chunk) != next(chunk)
    assert len(next(chunk)) == len(next(chunk)) == random_hexdump.CHUNK_SIZE


def test_render_hex():
    chunk = 0xABCDEF.to_bytes(8, 'big')
    hexed = random_hexdump.render_hex(chunk, 0, 0)
    assert hexed == '00 00 00 00 00 AB CD EF'


def test_render_ascii():
    chunk = b'ABCDEF'
    asciied = random_hexdump.render_ascii(chunk, 0, 0)
    assert asciied == 'ABCDEF'


def test_render_ascii_non_printable():
    chunk = b'\x0ABCDEF'
    asciied = random_hexdump.render_ascii(chunk, 0, 0)
    assert asciied == '.BCDEF'

