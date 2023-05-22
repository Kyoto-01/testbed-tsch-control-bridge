from configparser import ConfigParser


def configure_from_file(file: 'str'):
    config = {}

    conf = ConfigParser()

    conf.read(file)
    
    config['addr'] = conf['api']['addr']
    config['port'] = conf['api']['port']
    config['baddr'] = conf['broker']['addr']
    config['bport'] = conf['broker']['port']
    config['bqueue'] = conf['broker']['queue']

    return config
