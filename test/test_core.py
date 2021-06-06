import json
import unittest

from dictCLI import cache, core


class TestEnglish(unittest.TestCase):
    def setUp(self) -> None:
        self.result = core._fetch_meaning('hello')
        with open('test/fixtures/hello.json') as f:
            self.hello_meaning = json.load(f)[0]

    def test_response_value(self):
        self.assertEqual(self.result, self.hello_meaning,
                         "response from url should be robust")

    def test_response_type(self):
        self.assertEqual(type(self.result), dict,
                         "result from url should be a list of dict")

    def test_cache_meaning(self):
        file = '/home/chaitanya/.cache/english/favorites.json'
        cache.cache_meaning(self.result, file)
        with open(file) as f:
            cached_meaning = json.load(f)
        self.assertEqual(self.result, cached_meaning)


if __name__ == "__main__":
    unittest.main()
