from dictCLI import cache,core
import unittest 
import json 
import os 

class TestCache(unittest.TestCase):
    def setUp(self):
        self.data_dir = cache.get_data_dir()

    def test_get_data_dir(self):
        expected = os.path.join(os.environ.get('LOCALAPPDATA',''),'dictCLI')
        self.assertEqual(self.data_dir,expected)


    def test_word_cache(self):
        test_json = {'testkey':'testvalue'}
        cache.cache_meaning(test_json,'test_word')
        filepath = os.path.join(self.data_dir,'word_cache','test_word.json')
        self.assertTrue(os.path.isfile(filepath))

        with open(filepath) as f:
            self.assertDictEqual(test_json,json.load(f))


if __name__ == "__main__":
    unittest.main()
