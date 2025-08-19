import configparser

CONFIG_NAME = 'config.ini'

config = configparser.ConfigParser(interpolation=None)
config.read(CONFIG_NAME)
