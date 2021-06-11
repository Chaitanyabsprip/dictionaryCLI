from abc import ABC, abstractmethod
from typing import Dict, List


class Definition:
    def __init__(self):
        self._meanings: Dict[str, str]
        self._synonyms: List[str]
        self._antonyms: List[str]
        self._examples: List[str]
        self._pronounciations: List[str]
        self._audio: List[str]


class Word:
    def __init__(self):
        self.definitons: List[Definition]


class DictionarySource(ABC):
    pass


class Dictionary:
    def __init__(self, source: DictionarySource):
        self.source = source
        pass
