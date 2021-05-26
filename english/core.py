from wiktionaryparser import WiktionaryParser

PARSER = WiktionaryParser()


def get_meaning(word):
    return PARSER.fetch(word)


def cache_meaning(word_meaning):
    pass
