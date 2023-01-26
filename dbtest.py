import sqlite3 
import datetime


def create_db():
    with sqlite3.connect("test.db") as conn:
        cursor = conn.cursor()
        sql = "CREATE TABLE IF NOT EXISTS test (date timestamp not null);"
        cursor.execute(sql)

        sql = "INSERT INTO test (date) VALUES (?);"
        dd = datetime.datetime.now()
        cursor.execute(sql, [dd])

        dd = "dummy test"
        cursor.execute(sql, [dd])


    print ("111")
    with sqlite3.connect("test.db") as conn0:
        dttest(conn0)        

    print ("222")
    with sqlite3.connect("test.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn1:
        dttest(conn1)        



def dttest(conn):
    cursor = conn.cursor()
    sql = "SELECT date FROM test;"
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        for c in row:
            print (c, type(c))


create_db()

