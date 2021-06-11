from unittest import TestCase, main

from dictcli.config import Config
from dictcli.util import get_mode


class TestModes(TestCase):
    def setUp(self) -> None:
        self.commands: dict = Config()["commands"]
        self.mode_search1 = get_mode(':s')
        self.mode_search2 = get_mode(':search')
        self.mode_flip1 = get_mode(':f')
        self.mode_flip2 = get_mode(':flip')

    def test_quit(self):
        with self.assertRaises(SystemExit) as cm:
            get_mode(':q')
        self.assertEqual(cm.exception.code, 1)
        with self.assertRaises(SystemExit) as cm:
            get_mode(':quit')
        self.assertEqual(cm.exception.code, 1)

    def test_search(self):
        self.assertEqual(self.mode_search1, 'search')
        self.assertEqual(self.mode_search2, 'search')

    def test_flip(self):
        self.assertEqual(self.mode_flip1, 'flip')
        self.assertEqual(self.mode_flip2, 'flip')


if __name__ == "__main__":
    main()
