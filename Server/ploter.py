# coding: utf8
import log
import db_work
from config import cfg



import random
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import math
import datetime
import time
import sys


while True:
    x = []
    y = []
    z = []
    time_n = datetime.datetime.now()
    big_data = db_work.get_data(time_n - datetime.timedelta(hours=3), time_n)
    for i in big_data:
          x.append(i[0])
          y.append(i[1])
          z.append(i[2])

      # plot



    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    g = [time_n-datetime.timedelta(hours=3)+datetime.timedelta(minutes=15*i) for i in range(13)]
    plt.xticks(g,[i.strftime("%H:%M")for i in g])

    ax2 = ax.twinx()
    ax2.plot(x,z, label="Humidity", color='r')
    ax.plot(x,y, label="Temperature", color='b')
    ax.legend(loc='upper left')
    ax2.legend(loc='upper right')

    ax.grid(True)
    fig.autofmt_xdate()
      # beautify the x-labels
    plt.savefig("../static/3h.png")



    time_n = datetime.datetime.now()
    big_data = db_work.get_data(time_n - datetime.timedelta(hours=24), time_n)
    for i in big_data:
            x.append(i[0])
            y.append(i[1])
            z.append(i[2])

        # plot



    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    g = [time_n-datetime.timedelta(hours=24)+datetime.timedelta(hours=2*i) for i in range(13)]
    plt.xticks(g,[i.strftime("%H:%M")for i in g])

    ax2 = ax.twinx()
    ax2.plot(x,z, label="Humidity", color='r')
    ax.plot(x,y, label="Temperature", color='b')
    ax.legend(loc='upper left')
    ax2.legend(loc='upper right')

    ax.grid(True)
    fig.autofmt_xdate()
        # beautify the x-labels



    plt.savefig("../static/24h.png")

    print("Ploted!")
    time.sleep(180)
