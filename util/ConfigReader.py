import configparser

class ConfigReader:

    def __init__(self):
        pass

    @staticmethod
    def load_config(filename):

        parser = configparser.ConfigParser(interpolation=None)
        parser.read(filename)
        confdict = {section: dict(parser.items(section)) for section in parser.sections()}
        return confdict