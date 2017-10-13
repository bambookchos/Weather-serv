import yaml
import sys
import os

import log

CONFIG_FILE_NAME = "config.yml"

class Config(object):
    def __init__(self, conf_yml_file):
        if (not os.path.exists(conf_yml_file)):
            log.logging.critical('Config file not found!')
            sys.exit(-1)
        with open(conf_yml_file,'r') as stream:
            try:
                data = yaml.load(stream)
            except yaml.YAMLError:
                log.logging.critical('Error in config file!')
                sys.exit(-1)

            self.__mysql = data['mysql']


    def get(self, arg):
        if (arg == "mysql"):
            return self.__mysql
        else:
            log.logging.error('Unknown config request!')

cfg = Config(CONFIG_FILE_NAME)
