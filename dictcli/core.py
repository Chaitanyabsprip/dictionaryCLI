from colorama.ansi import Fore, Style
from wiktionaryparser import WiktionaryParser

from dictcli.bookmarks import Bookmarks, bookmark
from dictcli.cache import (add_to_history, cache_meaning, get_cached_meaning,
                           get_history)

PARSER = WiktionaryParser()


def _fetch_meaning(word: str) -> dict:
    """
        Returns the meaning of the query `@word` from API
    """
    meaning = PARSER.fetch(word)[0]
    if len(meaning['definitions']) == 0:
        return {}
    return meaning


def get_meaning(word: str):
    meaning = get_cached_meaning(word)
    if not meaning:
        meaning = _fetch_meaning(word)
        cache_meaning(meaning, word)
    return meaning


def pretty_print(meaning_json: dict) -> None:
    """
        Prints formatted string of the given meaning
    """

    if 'defintions' in meaning_json.keys():
        for definition in meaning_json['definitions']:
           print(f"{'-'*80}")
           print("{}{}:{}".format(Fore.GREEN, definition['partOfSpeech'].title(),
                               Style.RESET_ALL))
            for n, meaning in enumerate(definition['text']):
                print(f"\t{n}. {meaning}")
            for related_words in definition['relatedWords']:
                print(related_words['relationshipType'])
                for word in related_words['words']:
                    print(word)
    else:
        print('No meaning found')


def search_mode(inp: str):
    if inp == '/b':
        bookmark(get_history())
        return {}
    try:
        meaning = get_cached_meaning(inp)
    except FileNotFoundError:
        meaning = _fetch_meaning(inp)
        cache_meaning(meaning, inp)
    add_to_history(inp)
    return meaning


def flip_mode(inp: str, commands: dict) -> None:
    # !FIXME: calling get_bookmarks() each time an input is given
    bookmarks = Bookmarks()
    if inp in commands["randomize"]:
        bookmarks.randomize()
        print("randomized")
    elif inp in commands["next"]:
        word = bookmarks.next()
        print(word)
        pretty_print(get_meaning(word))
    elif inp in commands["prev"]:
        word = bookmarks.prev()
        print(word)
        pretty_print(get_meaning(word))
    print(bookmarks.current)
