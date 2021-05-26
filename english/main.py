#! /usr/bin/python3

import sys

from english import core

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please specify a word")
        sys.exit(1)
    query: str = sys.argv[1]
    core.pretty_print(core.get_meaning(query))
