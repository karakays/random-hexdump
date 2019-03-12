import sys

from .random_bytes import run


if __name__ == '__main__':
    txt = sys.argv[1] if len(sys.argv) > 1  else None
    run(txt)
