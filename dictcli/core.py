from colorama.ansi import Fore, Style
from wiktionaryparser import WiktionaryParser

from dictcli.bookmarks import Bookmarks
from dictcli.cache import add_to_history, cache_meaning, get_cached_meaning
from dictcli.util import is_connected

PARSER = WiktionaryParser()


def _fetch_meaning(word: str) -> dict:
    """
        Retreive the meaning of the query `@word` from API
    """
    if not is_connected():
        raise ConnectionError

    meaning = PARSER.fetch(word)
    if meaning:
        meaning = meaning[0]
        if len(meaning['definitions']) != 0:
            return meaning
    return {}


def get_meaning(word: str):
    word = word.lower()
    meaning = get_cached_meaning(word)
    if not meaning:
        meaning = _fetch_meaning(word)
        cache_meaning(meaning, word)
    return meaning


def pretty_print(meaning_json: dict) -> None:
    """
        Prints formatted string of the given meaning
    """
    if 'definitions' in meaning_json.keys():
        for definition in meaning_json['definitions']:
            print(f"{'-'*80}")
            print("{}{}:{}".format(Fore.BLUE,
                                   definition['partOfSpeech'].title(),
                                   Style.RESET_ALL))
            for n, meaning in enumerate(definition['text']):
                print(f"\t{n}. {meaning}")
            for related_words in definition['relatedWords']:
                foreground: str
                if (related_words["relationshipType"] == 'synonyms'):
                    foreground = Fore.GREEN
                else:
                    foreground = Fore.RED
                print("{}{}{}".format(foreground,
                                      related_words['relationshipType'],
                                      Style.RESET_ALL))
                for word in related_words['words']:
                    print('\t' + word)
    else:
        print('No meaning found')


def search_mode(inp: str):
    meaning = get_meaning(inp)
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
