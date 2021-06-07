#! /usr/bin/env python

from config import CONFIG
from dictCLI import core, util


def main() -> None:
    commands: dict = CONFIG["commands"]
    mode = "search"

    while (True):
        print(f"{mode} >", end=" ")
        inp: str = input()
        if len(inp) > 0 and inp[0] == ':':
            mode: str = util.get_mode(inp, commands)
        elif mode == "search":
            core.search_mode(inp)
        elif mode == "flip":
            core.flip_mode(inp, commands["inflip"])
        else:
            print("Invalid query or command")
            util.print_usage()


if __name__ == "__main__":
    util.print_usage()
    main()
