from unittest import TestCase

from dictcli.definitions import Definition, WordMeaning
from dictcli.dictionary import DictionarySource, Wiktionary


class TestWiktionary(TestCase):
    def setUp(self) -> None:
        self.word_meaning: WordMeaning
        self.definition1: Definition

    def test_get_meaning(self) -> None:
        pass
