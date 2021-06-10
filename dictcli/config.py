import yaml

if __name__ == '__main__':

    stream = open("../config.yml", 'r')
    dictionary = yaml.load(stream)
    # for key, value in dictionary.items():
    #     print(key + " : " + str(value))
    print(dictionary.items())
    stream.close()
