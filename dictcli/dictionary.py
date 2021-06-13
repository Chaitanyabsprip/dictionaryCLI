from abc import ABC, abstractmethod
from typing import Set

from wiktionaryparser import WiktionaryParser

from dictcli.definitions import Definition, WordMeaning


class DictionarySource(ABC):
    @abstractmethod
    def get_meaning(self, word: str) -> WordMeaning:
        pass


class Dictionary:
    def __init__(self, source: DictionarySource):
        self.source = source
        pass


class Wiktionary(DictionarySource):
    def __init__(self):
        self.parser = WiktionaryParser()

    def get_meaning(self, word: str) -> WordMeaning:
        response: dict = self.parser.fetch(word)[0]
        word_meaning: list = []
        tdefn: dict = {}
        for definition in response['definitions']:
            tdefn['relatedWords'] = []
            tdefn['partOfSpeech'] = definition.get('partOfSpeech', {''})
            tdefn['meanings'] = set(definition.get('text', {''}))
            for related_words in definition.get('relatedWords', []):
                if related_words['relationshipType'] == 'synonyms':
                    tdefn['synonyms'] = related_words['words']
                elif related_words['relationshipType'] == 'antonyms':
                    tdefn['antonyms'] = related_words['words']
                else:
                    tdefn['relatedWords'].extend(related_words['words'])

            word_meaning.append(
                Definition(
                    partOfSpeech=tdefn['partOfSpeech'],
                    meanings=tdefn['meanings'],
                    synonyms=tdefn['synonyms'],
                    antonyms=tdefn['antonyms'],
                    relatedWords=tdefn['relatedWords'],
                    examples=tdefn['examples'],
                ))

        return WordMeaning(
            Set(word_meaning),
            pronounciation=response['pronounciations'].get('text', []),
            audio=response.get('audio', []),
        )
