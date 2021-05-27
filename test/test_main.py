import io
import unittest
from unittest import mock
from unittest.mock import patch

from config import CONFIG
from dictCLI import main


class TestModes(unittest.TestCase):
    def setUp(self) -> None:
        self.commands: dict = CONFIG["commands"]
        self.mode_search1 = main.get_mode(':s', self.commands)
        self.mode_search2 = main.get_mode(':search', self.commands)
        self.mode_flip1 = main.get_mode(':f', self.commands)
        self.mode_flip2 = main.get_mode(':flip', self.commands)

    def test_quit(self):
        with self.assertRaises(SystemExit) as cm:
            main.get_mode(':q', self.commands)
        self.assertEqual(cm.exception.code, 1)
        with self.assertRaises(SystemExit) as cm:
            main.get_mode(':quit', self.commands)
        self.assertEqual(cm.exception.code, 1)

    def test_search(self):
        self.assertEqual(self.mode_search1, 'search')
        self.assertEqual(self.mode_search2, 'search')

    def test_flip(self):
        self.assertEqual(self.mode_flip1, 'flip')
        self.assertEqual(self.mode_flip2, 'flip')


if __name__ == "__main__":
    unittest.main()
