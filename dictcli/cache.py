from datetime import datetime
# from errno import ENOENT
from json import dump as json_dump
from json import load
# from os import environ, strerror
from os import environ
# from os.path import isfile, join
from os.path import join
from platform import system


def get_data_dir() -> str:
    dir_path: str = {
        'Windows': join(environ.get('LOCALAPPDATA', ''), 'dictCLI'),
        'Linux': join(environ.get('HOME', ''), '.cache', 'dictCLI'),
    }[system()]
    return dir_path


def cache_meaning(word_json: dict, word: str) -> None:
    filepath = join(CACHE_DIR, f'{word}.json')
    with open(filepath, 'w') as f:
        json_dump(word_json, f)


def add_to_history(word: str) -> None:
    with open(join(get_data_dir(), 'history.txt'), 'a+') as f:
        history = f.read().split('\n')[:-1]
        if word in history:
            history.remove(word)
        f.write(f'[{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}] {word}\n')


def get_history(word: str = None, index: int = -1):
    with open(join(get_data_dir(), 'history.txt'), 'r') as f:
        history = f.read().split('\n')[:-1]
    if not index:
        return history

    if word:
        return list(filter(lambda value: value[22:] == word, history))[0][22:]
    return history[index][22:]


def get_bookmarks() -> list:
    with open(join(get_data_dir(), 'bookmarks.txt')) as f:
        return f.read().split('\n')[:-1]


def get_cached_meaning(word):
    filepath = join(CACHE_DIR, f'{word}.json')
    try:
        with open(filepath, 'r') as f:
            return load(f)
    except FileNotFoundError:
        return None


CACHE_DIR = join(get_data_dir(), 'word_cache')
