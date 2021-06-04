import sys

from dictCLI import core


def get_mode(inp: str, commands: dict) -> str:
    cmd: str = inp[1:]
    mode: str = "search"
    if cmd in commands["help"]:
        print_help()
    elif cmd in commands["quit"]:
        sys.exit(1)
    elif cmd in commands["search"]:
        mode = "search"
    elif cmd in commands["flip"]:
        mode = "flip"
    else:
        print('Not a valid command')
    return mode


def search_mode(inp: str) -> None:
    if inp == '/b':
        core.bookmark()
    meaning = core.get_meaning(inp)
    core.pretty_print(meaning)


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
    Search        ':search', ':s'
    Flip          ':flip', ':f' 

Commands: 
    Help          ':help', ':h'
    Quit          ':quit', ':q'
    '''
    print(help)


def print_usage() -> None:
    print_help()
