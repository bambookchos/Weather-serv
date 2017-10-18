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

def aver(a,n):
    b = [0 for i in range(len(a))]
    for i in range(1,n):
        for j in range(0,i*2+1):
            b[i]+=a[j]
        b[i] = b[i]/(i*2+1)


        for j in range(0,i*2+1):
            b[len(a)-1-i]+=a[len(a)-1-j]
        b[len(a)-1-i] = b[len(a)-1-i]/(i*2+1)

    for i in range(n,len(a)-n):
        b[i] = a[i]
        for j in range(1,n+1):
            b[i]+=a[i-j]+a[i+j]
        b[i] = b[i]/(n*2+1)
    b[len(a)-1] = a[len(a)-1]
    b[0]=a[0]
    return b
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




    y = aver(y,4)
    z = aver(z,4)

    fig = plt.figure(figsize=(10,10))
    g = [time_n-datetime.timedelta(hours=3)+datetime.timedelta(minutes=15*i) for i in range(13)]
    ax = fig.add_subplot(111)
    ax2 = ax.twinx()

    ax.set_xticks(g)
    ax2.set_xticks(g)
    ax.set_xticklabels([i.strftime("%H:%M")for i in g])
    ax2.set_xticklabels([i.strftime("%H:%M")for i in g])

    ax.plot(x,y, label="Temperature", color='b')
    ax2.plot(x,z, label="Humidity", color='r')
    ax.legend(loc='upper left')
    ax2.legend(loc='upper right')

    ax.grid(True)
    plt.savefig("../static/3h.png")


    x = []
    y = []
    z = []

    time_n = datetime.datetime.now()
    big_data = db_work.get_data(time_n - datetime.timedelta(hours=24), time_n)
    for i in big_data:
            x.append(i[0])
            y.append(i[1])
            z.append(i[2])

        # plot
    y = aver(y,7)
    z = aver(z,7)
    fig = plt.figure(figsize=(10,10))
    g = [time_n-datetime.timedelta(hours=24)+datetime.timedelta(hours=2*i) for i in range(13)]
    ax = fig.add_subplot(111)
    ax2 = ax.twinx()

    ax.set_xticks(g)
    ax2.set_xticks(g)
    ax.set_xticklabels([i.strftime("%H:%M")for i in g])
    ax2.set_xticklabels([i.strftime("%H:%M")for i in g])

    ax.plot(x,y, label="Temperature", color='b')
    ax2.plot(x,z, label="Humidity", color='r')

    ax.legend(loc='upper left')
    ax2.legend(loc='upper right')

    ax.grid(True)
        # beautify the x-label

    plt.savefig("../static/24h.png")



    x = []
    y = []
    z = []

    time_n = datetime.datetime.now()
    big_data = db_work.get_data(time_n - datetime.timedelta(days=30), time_n)
    for i in big_data:
            x.append(i[0])
            y.append(i[1])
            z.append(i[2])

        # plot


    y = aver(y,25)
    z = aver(z,25)
    fig = plt.figure(figsize=(10,10))
    g = [(time_n-datetime.timedelta(days=30)).replace(hour=0,minute=0,second=0)+datetime.timedelta(days=i) for i in range(32)]
    ax = fig.add_subplot(111)
    ax.grid(True)
    ax2 = ax.twinx()


    ax.set_xticks(g)
    ax2.set_xticks(g)
    ax.set_xticklabels([i.strftime("%d %b")for i in g])
    ax2.set_xticklabels([i.strftime("%d %b")for i in g])
    ax.plot(x,y, label="Temperature", color='b')
    ax2.plot(x,z, label="Humidity", color='r')
    ax.legend(loc='upper left')
    ax2.legend(loc='upper right')


    # fig.autofmt_xdate()
        # beautify the x-labels




    plt.savefig("../static/30d.png")

    print("Ploted!")
    time.sleep(180)
