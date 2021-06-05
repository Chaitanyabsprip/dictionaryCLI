import json
import os
import platform
from datetime import datetime


def get_data_dir() -> str:
    dir_path: str = {
        'Windows': os.path.join(os.environ.get('LOCALAPPDATA', ''), 'dictCLI'),
        'Linux': os.path.join(os.environ.get('HOME', ''), '.cache', 'dictCLI'),
    }[str(platform.system())]
    if not os.path.exists(dir_path):  # TODO: refactor this to setup.py
        os.mkdir(dir_path)
        os.mkdir(os.path.join(dir_path, 'word_cache'))
    return dir_path


def cache_meaning(word_json, word):
    filepath = os.path.join(cache_dir, f'{word}.json')
    with open(filepath, 'w') as f:
        json.dump(word_json, f)


def add_to_history(word):
    with open(os.path.join(get_data_dir(), 'history.txt'), 'a') as history:
        history.write(
            f'[{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}] {word}\n')


def get_history(word: str, index: int = -1):
    with open(os.path.join(get_data_dir(), 'history.txt'), 'r') as f:
        history = f.read().split('\n')[:-1]

    for i in range(len(history)):
        history[i] = history[i].strip()

    if word:
        for entry in history:
            if word in entry and len(entry) == (len(word) + 22): return entry
    return history[index][22:]


def get_cached_meaning(word):
    filepath = os.path.join(cache_dir, f'{word}.json')
    if os.path.isfile(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    else:
        return None


cache_dir = os.path.join(get_data_dir(), 'word_cache')
