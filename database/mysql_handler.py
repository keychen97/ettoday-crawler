import pymysql
from config.settings import DB_CONFIG

def save_to_mysql(all_news):
    conn = None
    cursor = None

    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()

        create_table_sql = """
        CREATE TABLE IF NOT EXISTS ettoday_news (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT,
            content LONGTEXT
        )
        """
        cursor.execute(create_table_sql)

        insert_sql = "INSERT INTO ettoday_news (title, content) VALUES (%s, %s)"

        for title, content in all_news:
            cursor.execute(insert_sql, (title, content))

        conn.commit()
        print("資料成功寫入 MySQL")

    except Exception as e:
        print("發生錯誤：", e)

        if conn:
            conn.rollback()

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()