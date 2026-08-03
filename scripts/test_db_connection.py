from etl_pipeline.config import get_connection

try:
    conn = get_connection()

    cur = conn.cursor()

    cur.execute("SELECT version();")

    print(cur.fetchone()[0])

    cur.close()

    conn.close()

except Exception as e:
    print(e)