from typing import Set


class Definition:
    def __init__(
        self,
        partOfSpeech: str,
        meanings: Set[str],
        synonyms: Set[str],
        antonyms: Set[str],
        relatedWords: Set[str],
        examples: Set[str],
    ):
        self._partOfSpeech: str = partOfSpeech
        self._meanings: Set[str] = meanings
        self._synonyms: Set[str] = synonyms
        self._antonyms: Set[str] = antonyms
        self._examples: Set[str] = examples
        self._related_words: Set[str] = relatedWords

    def get_partOfSpeech(self) -> str:
        return self._partOfSpeech

    def get_meanings(self) -> Set[str]:
        return self._meanings

    def get_synonyms(self) -> Set[str]:
        return self._synonyms

    def get_antonyms(self) -> Set[str]:
        return self._antonyms

    def get_examples(self) -> Set[str]:
        return self._examples

    def get_related_words(self) -> Set[str]:
        return self._related_words


class WordMeaning:
    def __init__(self, definitions: Set[Definition], pronounciation: Set[str],
                 audio: Set[str]):
        self._pronounciations: Set[str] = pronounciation
        self._audio: Set[str] = audio
        self.definitons: Set[Definition] = definitions

    def get_pronounciations(self) -> Set[str]:
        return self._pronounciations

    def get_audio(self) -> Set[str]:
        return self._audio
