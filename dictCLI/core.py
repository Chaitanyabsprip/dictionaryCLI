import os

from wiktionaryparser import WiktionaryParser

from dictCLI import cache

PARSER = WiktionaryParser()


def fetch_meaning(word: str) -> dict:
    """
        Returns the meaning of the query `@word`
    """
    # TODO: raise errors when there are no definitions to for a given word
    return PARSER.fetch(word)[0]


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
    # TODO: BOOKMARK
    # if inp == '/b':
    # bookmark(get_history(-1))
    # return
    meaning = cache.get_cached_meaning(inp)
    if not meaning:
        meaning = fetch_meaning(inp)
        cache.cache_meaning(meaning, inp)
        cache.add_to_history(inp)
    pretty_print(meaning)


def flip_mode(inp: str, commands: dict) -> None:
    if inp in commands["randomize"]:
        print("bookmarked words randomised")
    elif inp in commands["next"]:
        print("next bookmark")
    elif inp in commands["prev"]:
        print("prev bookmark")


def bookmark(word: str) -> None:
    with open(os.path.join(cache.cache_dir, 'bookmarks.txt'), 'a') as f:
        f.write(word)
    print(f'{word} has been bookmarked \n')
