import cx_Oracle
import os
import pandas as pd
os.putenv('NLS_LANG', '.UTF8')
cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_10")
con_ip = "localhost:1521/xe"
con_id = "hr"
con_pw = "hr"
connection = cx_Oracle.connect(con_id, con_pw, con_ip)
cursor = connection.cursor()

data = pd.read_csv("sise2.csv", encoding="euc-kr")
data = pd.DataFrame(data)

pre = list(data.iloc[0:, 0])
vol = list(data.iloc[0:, 1])
print(pre)
print(vol)
print(len(pre))
print(len(vol))

for i in range(0, len(pre)):
    sql = "insert into kakao values(:1, :2)"
    insert = pre[i], vol[i]

    cursor.execute(sql, insert)
    connection.commit()