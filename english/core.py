from wiktionaryparser import WiktionaryParser

PARSER = WiktionaryParser()


def get_meaning(word):
    return PARSER.fetch(word)[0]


def cache_meaning(word_meaning):
    pass


def pretty_print(meaning_json):
    for parts_of_speech in meaning_json["definitions"]:
        print(f'Part of speech: {parts_of_speech["partOfSpeech"]}')
        meanings = parts_of_speech["text"]
        for i in range(1, len(meanings)):
            print(f'\t{meanings[i]}')
