import pymysql
from datetime import datetime
from io import StringIO

from flask import Flask
app = Flask(__name__)


app.route('/')
def index():
    stream = StringIO()
    db = MysqlDatabase()
    return ""
    


MYSQL_CONFIG = {'host': '192.168.1.253',
                'port': 20002,
                'user': 'chenzikun',
                'password': 'ppwchenzikun',
                'db': 'xw',
                'charset': 'utf8mb4'
                }


class MysqlDatabase(object):
    def __init__(self):
        pass

    @staticmethod
    def mysql_conn():
        return pymysql.connect(**MYSQL_CONFIG)

    def insert(self, sql, value):
        conn = self.mysql_conn()
        with conn.cursor() as cursor:
            cursor.execute(sql, value)
        conn.commit()

    def query(self, sql):
        with self.mysql_conn().cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    @staticmethod
    def date_time():
        return datetime.now().strftime('%H:%M:%S')

if __name__ == '__main__':
    app.run(debug=True)