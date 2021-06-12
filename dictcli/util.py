from sys import exit
from typing import List

from dictcli.config import Config


def get_mode(inp: str) -> str:
    commands = Config.commands
    cmd: str = inp[1:]
    mode: str = "search"
    if cmd in commands["help"]:
        print_help()
    elif cmd in commands["quit"]:
        exit(1)
    elif cmd in commands["search"]:
        mode = "search"
    elif cmd in commands["flip"]["cmd"]:
        mode = "flip"
    else:
        print('Not a valid command')
    return mode


def print_help() -> None:
    help: str = '''
Modes:
    Search        ':search', ':s'
    Flip          ':flip',   ':f' 

Commands: 
    Help          ':help',   ':h'
    Quit          ':quit',   ':q'
    '''
    print(help)


def print_usage() -> None:
    print_help()  # TODO : temporary


def write_list_to_file(word_list: List[str], filepath: str) -> None:
    with open(filepath, 'w') as f:
        for string in word_list:
            f.write(string)
