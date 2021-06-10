from yaml import FullLoader, load


class Config:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Config, cls).__new__(cls)
            cls.source = "wiktionary"
            cls.commands = {
                'help': ['h', 'help'],
                'quit': ['q', 'exit', 'quit'],
                'search': ['s', 'search'],
                'flip': {
                    'cmd': ['f', 'flip'],
                    'randomize': ['r', 'random'],
                    'next': ['n', 'j', ''],
                    'prev': ['p', 'k', '.']
                }
            }
            with open("config.yml", 'r') as f:
                config = load(f, Loader=FullLoader)
                cls.source = config['source']
                cls.commands = config['commands']

        # return cls.__instance
