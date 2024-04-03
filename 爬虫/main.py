# pip install pymysql
import pymysql
config = {
  'host':'127.0.0.1',
  'user':'root',
  'password':'KaiFa@00#99',
  'port':3306,
  'database':'tiktok_system',
}
# conn = pymysql.Connect(host='127.0.0.1',user='root',password='KaiFa@00#99',port=3306,database='tiktok_system')
# 获取到连接对象
conn = pymysql.Connect(**config)
# 获取操作数据游标
cur = conn.cursor()

sql = 'select * from tk_task where id=1'
cur.execute(sql)
print(cur.fetchall())
