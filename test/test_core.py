from json import load
from unittest import TestCase, main

from dictCLI.core import _fetch_meaning


class TestEnglish(TestCase):
    def setUp(self) -> None:
        self.result = _fetch_meaning('hello')
        with open('test/fixtures/hello.json') as f:
            self.hello_meaning = load(f)[0]

    def test_response_value(self):
        self.assertEqual(self.result, self.hello_meaning,
                         "response from url should be robust")

    def test_response_type(self):
        self.assertEqual(type(self.result), dict,
                         "result from url should be a list of dict")


if __name__ == "__main__":
    main()
