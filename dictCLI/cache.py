import platform
import os
import json
platform = platform.system()

def get_data_dir():
    return {
        'Windows' : os.path.join(os.environ.get('LOCALAPPDATA',''),'dictCLI'),
        'Linux' : os.path.join(os.environ.get('HOME',''),'.cache/dictCLI'),
    }[platform]

def cache_meaning(word_json,word):
    cache_dir = os.path.join(get_data_dir(),'word_cache')
    filepath = os.path.join(cache_dir, f'{word}.json')
    with open(filepath, 'w') as f:
        json.dump(word_json, f)

