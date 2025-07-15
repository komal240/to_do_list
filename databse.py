import psycopg2

conn=psycopg2.connect(
host="localhost",
database="TO_DO_LIST",
user="postgres",
password="Komal@123",
port="5432"
)

cur=conn.cursor()

def query(q):
    cur.execute(q)
    if q.strip().lower().startswith("select"):
        result=cur.fetchall()
        return result
    else:
        conn.commit()
        return 0