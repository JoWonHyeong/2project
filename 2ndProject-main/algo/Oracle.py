import cx_Oracle
import os

os.putenv('NLS_LANG', '.UTF8')
cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_10")
con_ip = "localhost:1521/xe"
con_id = "hr"
con_pw = "hr"
connection = cx_Oracle.connect(con_id, con_pw, con_ip)
cursor = connection.cursor()

def insert(stock):
    cursor.execute("insert into kakao values (:1, :2, sysdate)", (stock[0], stock[1]))
    connection.commit()

def select():
    cursor.execute("select * from kakao")
    data = cursor.fetchall()
    return data

def oneselect():
    cursor.execute("select * from kakao order by 시간 desc")
    data = cursor.fetchone()
    return data

def aldeldata():
    cursor.execute("TRUNCATE TABLE kakao")

def aldelvpin():
    cursor.execute("TRUNCATE TABLE vpin")

def insertV(vpin):
    vpin = str(vpin)
    cursor.execute("insert into vpin values( " + vpin + ")")
    connection.commit()

