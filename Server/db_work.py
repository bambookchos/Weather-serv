import pymysql

from config import cfg
import log


mysql_conf = cfg.get("mysql")
# TODO: cursor connect

db = pymysql.connect(host=mysql_conf["host"], user=mysql_conf["user"], passwd=mysql_conf["passwd"], db=mysql_conf["db"], charset=mysql_conf["charset"])


def get_data(data_start_time, end_date_time):
    cursor = db.cursor()
    sql = "SELECT th_time, temperature, humidity FROM data WHERE th_time between '{0}' AND '{1}'".format(data_start_time,data_end_time)
    cursor.execute(sql)
    data =  cursor.fetchall()
    return data

def get_last_data():
    cursor = db.cursor()
    sql = "SELECT th_time, temperature, humidity FROM data ORDER BY th_time DESC LIMIT 1"
    cursor.execute(sql)
    data =  cursor.fetchall()
    return data
