from wiktionaryparser import WiktionaryParser

from dictCLI import cache
from dictCLI.bookmarks import Bookmarks, bookmark

PARSER = WiktionaryParser()


def _fetch_meaning(word: str) -> dict:
    """
        Returns the meaning of the query `@word` from API
    """
    # TODO: raise errors when there are no definitions to for a given word
    return PARSER.fetch(word)[0]


def get_meaning(word: str):
    meaning = cache.get_cached_meaning(word)
    if not meaning:
        meaning = _fetch_meaning(word)
        cache.cache_meaning(meaning, word)
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
            for words in related_words['words']:
                pass


def search_mode(inp: str) -> None:
    if inp == '/b':
        try:
            bookmark(cache.get_history())
        catch e:
            print("No words bookmarked yet")
        return
    cache.add_to_history(inp)
    pretty_print(get_meaning(inp))


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
    print(len(bookmarks.words))
