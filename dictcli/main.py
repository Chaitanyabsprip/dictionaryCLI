#! /usr/bin/env python

from config import CONFIG
from dictcli.core import flip_mode, pretty_print, search_mode
from dictcli.util import get_mode, print_usage


def main() -> None:
    commands, mode = CONFIG["commands"], "search"
    print_usage()

    while (True):
        print(f"{mode} >", end=" ")
        inp: str = input()
        if len(inp) > 0 and inp[0] == ':':
            mode: str = get_mode(inp)
        elif mode == "search":
            pretty_print(search_mode(inp))
        elif mode == "flip":
            flip_mode(inp, commands["inflip"])
        else:
            print("Invalid query or command")
            print_usage()


if __name__ == "__main__":
    main()
