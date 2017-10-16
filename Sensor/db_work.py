import pymysql

from config import cfg
import log


mysql_conf = cfg.get("mysql")
# TODO: cursor connect


def add_data(data_time, data_temperature, data_humidity):
    try:
        db = pymysql.connect(host=mysql_conf["host"], user=mysql_conf["user"], passwd=mysql_conf["passwd"], db=mysql_conf["db"], charset=mysql_conf["charset"])
        cursor = db.cursor()
        sql="INSERT INTO data(th_time, temperature, humidity) VALUES ('{0}', '{1}', '{2}')".format(data_time, data_temperature, data_humidity)
        cursor.execute(sql)
        db.commit()
        log.logging.info("Added new temperature in DB!")
        db.close()
    except:
        log.logging.error("Error in DB!")




