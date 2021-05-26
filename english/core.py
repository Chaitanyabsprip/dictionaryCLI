import json
import os

from wiktionaryparser import WiktionaryParser

PARSER = WiktionaryParser()


def get_meaning(word):
    return PARSER.fetch(word)[0]


def cache_meaning(word_meaning, file):
    # dir = f"/home/chaitanya/.cache/english"  # TODO: refactor for cross-platform
    # if not os.path.isdir(dir):
    #     os.mkdir(dir)
    with open(file, 'w') as f:
        already_cached = []
        if os.path.isfile(file):
            already_cached = json.load(f)
        already_cached.append(word_meaning)
        json.dump(already_cached, f)


def pretty_print(meaning_json):
    for parts_of_speech in meaning_json["definitions"]:
        print(f'Part of speech: {parts_of_speech["partOfSpeech"]}')
        meanings = parts_of_speech["text"]
        for i in range(1, len(meanings)):
            print(f'\t{meanings[i]}')
