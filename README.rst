
=======
random-hexdump
=======

A hexdump implementation.

With the difference of, there is no input file, it generates random bytes and allows you to embed custom text into it.

The display format starts with the offset in hexadecimal, followed by 16 space-separated random hexadecimal bytes that contains your custom text and finally followed by the same sixteen bytes in ASCII representation.

Inspired by *Jamie Zawinski*'s homepage_.

---------------
Usage
---------------
.. highlight:: python
   :linenothreshold: 5

>>> import random-hex
>>> for line in dump(text = "selcuk karakayali")
...     print(f"line")
00000000 7E B0 14 53 85 42 07 E8 50 77 6A C6 05 D5 79 88 ~..S.B..Pwj...y.
00000010 AA BE 67 63 F2 4C 88 58 2B 38 C3 F3 D3 4D 6C AD ..gc.L.X+8...Ml.
00000020 8A 23 56 5C C0 71 3D 9F 28 AC C7 AF AA 57 34 72 .#V\.q=.(....W4r
00000030 37 E0 52 78 E2 9B 18 32 25 87 BA 0F 0B E2 2C EF 7.Rx...2%.....,.
00000040 AE EA F2 29 D1 39 BE 3A DC F8 13 7B C2 19 E9 F3 ...).9.:...{....
00000050 49 BF CF 55 A5 62 F7 73 65 6C 63 75 6B 20 6B 61 I..U.b.selcuk ka
00000060 72 61 6B 61 79 61 6C 69 5D 2D 5E A7 55 AF D9 B2 rakayali]-^.U...
00000070 DA 00 2A BB B6 57 9F E1 6D CA 7C AF 03 BC D3 7D ..*..W..m.|....}
00000080 8E E7 CC 49 0F 6E 49 90 FC 3D FC 4F 55 35 1C B0 ...I.nI..=.OU5..
00000090 CB DA 27 A1 EF AB 35 45 8C C9 3F 24 E6 07 2D 6B ..'...5E..?$..-k
000000A0 B1 29 43 5A EA BC 41 71 49 61 0D 28 71 C4 2F 02 .)CZ..AqIa.(q./.
000000B0 22 D2 D5 DD CC AC 21 0D 59 E7 46 2F A3 A3 10 BB ".....!.Y.F/....
000000C0 46 45 37 B0 2B 6D F9 BF 42 AD 06 B0 8B 3E 27 6F FE7.+m..B....>'o
000000D0 D3 2A E6 C0 5F FA A6 16 CF 91 ED 19 85 45 75 8E .*.._........Eu.
000000E0 B9 9F 9D C6 03 92 67 AB 11 8E 20 C5 26 7D 64 DE ......g... .&}d.

---------------
License
---------------

`MIT license`

---------------
Authors
---------------

Selçuk Karakayalı <skarakayali@gmail.com>

.. _homepage: https://jwz.org
