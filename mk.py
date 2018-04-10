#!/usr/bin/env python3

import sys


def LIST():
    import os
    os.system("grep '^# ' notes.md")


def is_command(f):
    """
    Return true when `f` is the name of a command
    that can be called from the command line.
    """
    return f.isupper()


def main(argv=None):
    if argv is None:
        argv = sys.argv

    arg = argv[1:]

    try:
        return globals()[arg[0].upper()]()
    except KeyError:
        pass

    for k in sorted(globals()):
        if is_command(k):
            print(k)

if __name__ == '__main__':
    sys.exit(main())
