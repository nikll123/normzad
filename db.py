# database 
# модуль для работы непосредственно с БД

import sqlite3 
import config

def create_db():
    with sqlite3.connect(config.dbFileName) as conn:
        cursor = conn.cursor()


        sql = """CREATE TABLE IF NOT EXISTS Departments(
            id   integer PRIMARY KEY AUTOINCREMENT, 
            Name text    NOT NULL
            );"""
        cursor.execute(sql)
        sql = """CREATE UNIQUE INDEX IF NOT EXISTS indexUniqueDepartments ON Departments(Name);"""
        cursor.execute(sql)


        sql = """CREATE TABLE IF NOT EXISTS Positions(
            id   integer PRIMARY KEY AUTOINCREMENT, 
            Name text    NOT NULL
            );"""
        cursor.execute(sql)
        sql = """CREATE UNIQUE INDEX IF NOT EXISTS indexUniquePositions ON Positions(Name);"""
        cursor.execute(sql)


        sql = """CREATE TABLE IF NOT EXISTS workers(
            TabelNom   integer PRIMARY KEY, 
            LastName   text    NOT NULL, 
            Name       text    NOT NULL, 
            SecondName text    NOT NULL,
            PositionId integer NOT NULL,
            Level      integer NOT NULL
            );"""
        cursor.execute(sql)


def getLastId(cursor):
    res = cursor.execute("Select last_insert_rowid()")
    res = res.fetchone()
    return res[0]


if __name__ == '__main__':
    create_db()

