import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="etl_pipeline_db",
        user="etl_user",
        password="Abhi30@shek",
        port=5432
    )

    cur = conn.cursor()

    cur.execute("SELECT version();")
    print("Connected Successfully!")
    print(cur.fetchone()[0])

    cur.close()
    conn.close()

except Exception as e:
    print("Connection Failed!")
    print(e)