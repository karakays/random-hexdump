
# random-hexdump

A stupid hexdump implementation for fun.

_rhd_ generates random bytes by allowing to embed custom text and outputs its dump.

The output is in conventional `hexdump` format which starts with the offset in hexadecimal followed by 16 space-separated hexadecimal bytes which might contain an optional input text and finally followed by the same sixteen bytes in ASCII representation.

## Usage

[![asciicast](https://asciinema.org/a/jKIS8YeB3mCLcF6xOBJ2iebSL.png?theme=tango&loop=1)](https://asciinema.org/a/jKIS8YeB3mCLcF6xOBJ2iebSL?theme=tango&loop=1)


<script src="https://asciinema.org/a/jKIS8YeB3mCLcF6xOBJ2iebSL.png" id="asciicast-14" async></script>

![demo](demo.svg)

## Inspired by

Jamie Zawinski's [personal homepage](https://jwz.org)

## License

`MIT license`

## Authors

Selçuk Karakayalı <skarakayali@gmail.com>

