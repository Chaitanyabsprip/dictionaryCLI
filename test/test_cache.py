from json import load
from os import environ
from os.path import isfile, join
from unittest import TestCase, main

from dictCLI.cache import cache_meaning, get_data_dir
from dictCLI.core import fetch_meaning


class TestCache(TestCase):
    def setUp(self):
        self.result = fetch_meaning('hello')
        self.data_dir = get_data_dir()

    def test_get_data_dir(self):
        expected = join(
            environ.get('LOCALAPPDATA', join(str(environ.get('HOME')),
                                             ".cache")), 'dictCLI')
        self.assertEqual(self.data_dir, expected)

    def test_word_cache(self):
        test_json = {'testkey': 'testvalue'}
        cache_meaning(test_json, 'test_word')
        filepath = join(self.data_dir, 'word_cache', 'test_word.json')
        self.assertTrue(isfile(filepath))

        with open(filepath) as f:
            self.assertDictEqual(test_json, load(f))

    def test_cache_meaning(self):
        file = '/home/chaitanya/.cache/dictCLI/word_cache/hello.json'
        cache_meaning(self.result, "hello")
        with open(file) as f:
            cached_meaning = load(f)
        self.assertEqual(self.result, cached_meaning)


if __name__ == "__main__":
    main()
