[![Build Status](https://travis-ci.org/karakays/random-hexdump.svg?branch=master)](https://travis-ci.org/karakays/random-hexdump)

# random-hexdump

A stupid `hexdump` implementation for fun.

`rhd` generates random bytes by allowing to embed custom text and outputs the dump.

The output is in conventional `hexdump` format which starts with the offset in hexadecimal followed by 16 space-separated hexadecimal bytes which might contain an optional input text and finally followed by the same sixteen bytes in ASCII representation.

## Usage

<p align="center">
  <img width="800" height="600" src="assets/demo.svg">
</p>

## Inspired by

Jamie Zawinski's [personal homepage](https://jwz.org)

## License

MIT license

## Authors

Selçuk Karakayalı <skarakayali@gmail.com>

