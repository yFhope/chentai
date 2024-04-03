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

class DB_Tools():
    def __init__(self):
        self.config = {
          'host':'127.0.0.1',
          'user':'root',
          'password':'KaiFa@00#99',
          'port':3306,
          'database':'tiktok_system',
        }
        self.conn = pymysql.Connect(**self.config)
        self.cur = self.conn.cursor()

    def query_all(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def insert_data(self,sql,data):
        self.cur.execute(sql,data)
        self.conn.commit()



