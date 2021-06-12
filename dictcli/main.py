#! /usr/bin/env python

from colorama import Fore, Style, init

from dictcli.config import Config
from dictcli.core import flip_mode, pretty_print, search_mode
from dictcli.util import get_mode, print_usage


def main() -> None:
    Config()
    init()
    commands, mode = Config.commands, "search"
    print_usage()

    while (True):
        print(f"{Fore.YELLOW}{Style.BRIGHT}{mode}>", end=f"{Style.RESET_ALL} ")
        inp: str = input()
        if len(inp) > 0 and inp[0] == ':':
            mode: str = get_mode(inp)
        elif mode == "search":
            pretty_print(search_mode(inp))
        elif mode == "flip":
            flip_mode(inp, commands["flip"])
        else:
            print("Invalid query or command")
            print_usage()


if __name__ == "__main__":
    main()
