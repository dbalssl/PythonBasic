import pymysql
import pymysql.cursors

# 네트워크
#  - IP: 컴퓨터 주소!
#     ㄴ 고정IP
#     ㄴ 유동IP
#     ㄴ 루프백IP: 127.0.0.1
#Python 프로그램과 Database 연결
def connection():
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="mariadb",
            database="chosum",
            charset="utf8",
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor
            
        )
        return conn
    except pymysql.Error as e:
        print(f"MariaDB 연결실패: {e}")