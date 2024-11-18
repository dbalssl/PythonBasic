from connection import connection

# MariaDB에 수집한 뉴스 저장
def insert_news(data: dict):
    # 1. Connection (P-D 연결)
    conn = connection()
    try:
        # 2. Cursor 객체 생성(일꾼 생성)
        curs = conn.cursor()
        # 3. SQL 작성(일 생성)
        sql = """
            INSERT INTO tbl_news(title, writer, content, regdate) 
            VALUES(%(title)s, %(writer)s, %(content)s, %(regdate)s);
        """
        # 4. Execute(실행)
        curs.execute(sql, data)
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()