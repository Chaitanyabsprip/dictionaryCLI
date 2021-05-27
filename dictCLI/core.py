import json
import os

from wiktionaryparser import WiktionaryParser

PARSER = WiktionaryParser()


def get_meaning(word):
    """
        Returns the meaning of the query `@word`
    """
    # TODO : raise errors when there are no definitions to for a given word
    return PARSER.fetch(word)[0]


def cache_meaning(word_meaning, file):
    # dir = f"/home/chaitanya/.cache/.dictCLI"  # TODO : refactor for cross-platform
    # if not os.path.isdir(dir):
    #     os.mkdir(dir)
    with open(file, 'w') as f:
        already_cached = []
        if os.path.isfile(file):
            already_cached = json.load(f)
        already_cached.append(word_meaning)
        json.dump(already_cached, f)


def pretty_print(meaning_json):
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
