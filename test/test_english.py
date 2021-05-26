import json
import unittest

from english import core


class TestEnglish(unittest.TestCase):
    def setUp(self) -> None:
        self.result = core.get_meaning('hello')
        with open('test/fixtures/hello.json') as f:
            self.hello_meaning = json.load(f)

    def test_response_value(self):
        self.assertListEqual(self.result, self.hello_meaning,
                             "response from url should be robust")

    def test_response_type(self):
        self.assertIsInstance(self.result, list,
                              "result from url should be a list of dict")


if __name__ == "__main__":
    unittest.main()
