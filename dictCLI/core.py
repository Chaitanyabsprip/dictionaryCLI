import json
import os
from dictCLI import cache
# cache = cache.Cache(callingmodule='core')
# cache = cache.Cache()
from wiktionaryparser import WiktionaryParser

PARSER = WiktionaryParser()
def get_meaning(word):
    """
        Returns the meaning of the query `@word`
    """
    # TODO : raise errors when there are no definitions to for a given word
    return PARSER.fetch(word)[0]
    

def add_to_history(word):
    with open(os.path.join(cache.get_data_dir(),'history.txt'),'a') as history:
        history.write(f'{word} \n')

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
