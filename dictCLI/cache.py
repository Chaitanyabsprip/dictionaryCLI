import json
import os
import platform


def get_data_dir() -> str:
    return {
        'Windows': os.path.join(os.environ.get('LOCALAPPDATA', ''), 'dictCLI'),
        'Linux': os.path.join(os.environ.get('HOME', ''), '.cache/dictCLI'),
    }[str(platform)]


platform = platform.system()
cache_dir: str = os.path.join(get_data_dir(), 'word_cache')


def cache_meaning(word_json: dict, word: str) -> None:
    filepath: str = os.path.join(cache_dir, f'{word}.json')
    with open(filepath, 'w') as f:
        json.dump(word_json, f)


def add_to_history(word: str):
    with open(cache_dir, 'a') as f:
        f.write(word)


def get_history():
    pass
