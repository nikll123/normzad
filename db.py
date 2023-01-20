# database 
# модуль для работы непосредственнго с БД

import sqlite3 

def create_db():
    with sqlite3.connect("normzad.db") as db:
        cursor = db.cursor()


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
            id         integer NOT NULL PRIMARY KEY, 
            LastName   text    NOT NULL, 
            Name       text    NOT NULL, 
            SecondName text    NOT NULL,
            PositionId integer NOT NULL,
            Level      integer NOT NULL
            );"""
        cursor.execute(sql)

create_db()
