from os.path import join
from typing import List

from wiktionaryparser import WiktionaryParser

from dictCLI.cache import (add_to_history, cache_meaning, get_cached_meaning,
                           get_data_dir, get_history)

PARSER = WiktionaryParser()


def fetch_meaning(word: str) -> dict:
    """
        Returns the meaning of the query `@word`
    """
    meaning = PARSER.fetch(word)[0]
    if len(meaning['definitions']) == 0: return {}
    return meaning


def pretty_print(meaning_json: dict) -> None:
    """
        Prints formatted string of the given meaning
    """
    for definition in meaning_json['definitions']:
        print(f"{'-'*20}")
        print(f"{definition['partOfSpeech'].title()}:")

        for n, meaning in enumerate(definition['text']):
            print(f"\t{n}. {meaning}")

        for related_words in definition['relatedWords']:
            print(related_words['relationshipType'])
            for word in related_words['words']:
                print(word)


def search_mode(inp: str):
    if inp == '/b':
        bookmark(get_history())
        return {}
    try:
        meaning = get_cached_meaning(inp)
    except FileNotFoundError:
        meaning = fetch_meaning(inp)
        cache_meaning(meaning, inp)
    add_to_history(inp)
    return meaning


def flip_mode(inp: str, commands: dict) -> None:
    if inp in commands["randomize"]:
        print("bookmarked words randomised")
    elif inp in commands["next"]:
        print("next bookmark")
    elif inp in commands["prev"]:
        print("prev bookmark")


def bookmark(word: str) -> None:
    with open(join(get_data_dir(), 'bookmarks.txt'), 'a+') as f:
        bookmarks: List[str] = f.read().split('\n')[:-1]
        if word not in bookmarks:
            f.write(word)
    print(f'{word} has been bookmarked \n')
