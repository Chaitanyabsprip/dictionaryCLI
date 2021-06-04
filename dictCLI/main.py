#! /usr/bin/python3
# TODO : cross-platform she-bang!

from config import CONFIG
from dictCLI import utils


def main() -> None:
    commands: dict = CONFIG["commands"]
    mode = "search"

    while (True):
        print(f"{mode}>", end=" ")
        inp: str = input()
        if len(inp) > 0 and inp[0] == ':':
            mode: str = utils.get_mode(inp, commands)
        elif mode == "search":
            utils.search_mode(inp)
        elif mode == "flip":
            utils.flip_mode(inp, commands["flip"])
        else:
            print("Invalid query or command")
            utils.print_usage()


if __name__ == "__main__":
    utils.print_usage()
    main()
