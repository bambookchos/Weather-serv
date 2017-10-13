# coding: utf8

import time
import sys
import Adafruit_DHT
import log
import db_work
from config import cfg
from datetime import datetime
sensor = Adafruit_DHT.AM2302
pin = 4

max_t = -100
min_t = 100
while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            db_work.add_data(datetime.now(),temperature,humidity)
        else:
                print('Failed to get reading. Try again!')
        time.sleep(15)
