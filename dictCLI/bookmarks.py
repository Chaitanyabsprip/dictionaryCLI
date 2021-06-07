import os
from random import shuffle
from typing import List

from dictCLI import cache


class Bookmarks:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Bookmarks, cls).__new__(cls)
            cls.words: list = cache.get_bookmarks()
            assert (len(cls.words) > 0)
            cls.current: int = -1
        return cls.__instance

    def next(self):
        if self.current < len(self.words) - 1:
            self.current += 1
        else:
            self.current = 0
        return self.words[self.current]

    def prev(self):
        if self.current > 0:
            self.current -= 1
        else:
            self.current = len(self.words) - 1
        return self.words[self.current]

    def randomize(self):
        shuffle(self.words)


def bookmark(word) -> None:
    with open(os.path.join(cache.get_data_dir(), 'bookmarks.txt'), 'a+') as f:
        bookmarks: List[str] = f.read().split('\n')[:-1]
        if word not in bookmarks:
            f.write(f'{word}\n')
    print(f'{word} bookmarked \n')