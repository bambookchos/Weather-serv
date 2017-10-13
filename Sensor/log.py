import logging

logging.basicConfig(format = '[%(asctime)s] [%(levelname)-8s] [%(filename)s:%(lineno)d] %(message)s', level = logging.DEBUG, filename = u'weather.log')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] [%(levelname)-8s] [%(filename)s:%(lineno)d] %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
