#! /usr/bin/python3
# TODO : cross-platform she-bang!
import sys

from config import CONFIG
from english import core


def main() -> None:
    commands: dict = CONFIG["commands"]

    while (True):
        inp: str = input()
        mode = str()
        if inp[0] == ':':
            cmd: str = inp
            if cmd in commands["help"]:
                print_help()
            elif cmd in commands["quit"]:
                exit()
            elif cmd[:2] in commands["search"]:
                mode = "search"
            elif cmd == "flip":
                mode = "flip"
        elif mode == "search":
            core.pretty_print(core.get_meaning(inp))
        elif mode == "flip":
            flip_mode(inp, commands["flip"])
        else:
            print("Invalid query or command")
            print_usage()


def flip_mode(inp: str, commands: dict) -> None:
    if inp in commands["randomize"]:
        print("bookmarked words randomised")
    elif inp in commands["next"]:
        print("next bookmark")
    elif inp in commands["prev"]:
        print("prev bookmark")


def print_help() -> None:
    help: str = '''
Modes:
    Search        'search', 's'
    Flip          'flip', 'f'

Commands: 
    Help          'help', 'h'
    Quit          'quit', 'q'
    '''
    print(help)


def print_usage() -> None:
    pass


if __name__ == "__main__":
    print_usage()
    main()
