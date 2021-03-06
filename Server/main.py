# coding: utf8
from wsgiref.simple_server import make_server
from cgi import parse_qs
import log
import db_work
from config import cfg



import random
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import math
import datetime


def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    data = db_work.get_last_data()[0]

    print(data)
    body="""
    <html>
    <head>
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
    <link href='https://fonts.googleapis.com/css?family=Lobster' rel='stylesheet'>
    <style>
    .block{{
        background:#fff;
        opacity:.7;
        padding:10px;
        border-radius:5px;
        width:800px;
        text-align:center;
        margin:auto
    }}
    body{{
        font-family:Lobster,cursive;
        background:url(lands.jpg) no-repeat;
        -moz-background-size:100%;
        -webkit-background-size:cover;
        -o-background-size:cover;
        background-size:cover
        }}
    h3{{
        font-size:30pt
    }}
    </style>
    <title>yadoTroF Weather</title>
    </head>

    <body>
    <div class="block">
    <img src="title.png" height="300px">
    <h3>Температура: {0} C°  , Влажнсть : {1}%<h3>
    <h3>Время замера {2}<h3>
    <h4>График температуры и влажности за последние 3 часа</h4>
    <img src="3h.png" height="700px">
    <h4>График температуры и влажности за последние 24 часа</h4>
    <img src="24h.png" height="700px">
    </div>
    </body>
    </html>
    """.format(data[1],data[2],data[0].strftime("%d %B %Y %I:%M%p"))



    body = body.encode('utf-8')
    return [body]

httpd = make_server('', 8082, application)
print ("Serving on port 8082...")

# Serve until process is killed
httpd.serve_forever()
