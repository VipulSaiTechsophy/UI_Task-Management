from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read(r'/home/vipulsai/PycharmProjects/pythonProject7/Configurations/config.ini')
    return config.get(section, key)