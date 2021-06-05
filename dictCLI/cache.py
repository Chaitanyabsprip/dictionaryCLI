import json
import os
import platform


def get_data_dir() -> str:
    dir_path: str = {
        'Windows': os.path.join(os.environ.get('LOCALAPPDATA', ''), 'dictCLI'),
        'Linux': os.path.join(os.environ.get('HOME', ''), '.cache', 'dictCLI'),
    }[str(platform)]
    return dir_path


def cache_meaning(word_json, word):
    filepath = os.path.join(cache_dir, f'{word}.json')
    with open(filepath, 'w') as f:
        json.dump(word_json, f)


def add_to_history(word):
    with open(os.path.join(data_dir, 'history.txt'), 'a') as history:
        history.write(f'{word} \n')


def get_history():
    pass


def get_cached_meaning(word):
    filepath = os.path.join(cache_dir, f'{word}.json')
    if os.path.isfile(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    else:
        return None


platform = platform.system()
data_dir = get_data_dir()
cache_dir = os.path.join(data_dir, 'word_cache')
