# database 
# модуль для работы непосредственно с БД

import sqlite3 
import config

def create_db():
    with sqlite3.connect(config.dbFileName, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn:
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
            TabelNom     integer PRIMARY KEY, 
            LastName     text    NOT NULL, 
            Name         text    NOT NULL, 
            SecondName   text    NOT NULL,
            PositionId   integer NOT NULL,
            Level        integer NOT NULL,
            DepartmentId integer NOT NULL,
            FOREIGN KEY(DepartmentId) REFERENCES Departments(id),
            FOREIGN KEY(PositionId) REFERENCES Positions(id)
            );"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS Tasks(
            id   integer PRIMARY KEY AUTOINCREMENT, 
            Name text    NOT NULL
            );"""
        cursor.execute(sql)
        sql = """CREATE UNIQUE INDEX IF NOT EXISTS indexUniquePositions ON Tasks(Name);"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS jobs(
            id           integer   PRIMARY KEY AUTOINCREMENT,
            TabelNom     integer   NOT NULL, 
            TaskId       integer   NOT NULL, 
            Date         timestamp NOT NULL, 
            TimeJob      integer   NOT NULL,
            Comment      text      NOT NULL,
            FOREIGN KEY(TabelNom) REFERENCES Workers(TabelNom),
            FOREIGN KEY(TaskId) REFERENCES Tasks(id)
            );"""
        cursor.execute(sql)

def getLastId(cursor):
    res = cursor.execute("Select last_insert_rowid()")
    res = res.fetchone()
    return res[0]

def execute(sql, data=[]):
    err = config.dummyErr
    resData = None
    with sqlite3.connect(config.dbFileName, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(sql, data)
            err = ''
            if 'INSERT' == sql[:6]:
                resData = getLastId(cursor)
        except Exception as ex: 
            err = f"SQL eror:\n   {sql}\n   {ex.args[0]}\n   data = {data}"
    return err, resData

def executeTry(sql, data=[]):
    err = config.dummyErr
    resData = None
    try:
        conn = sqlite3.connect(config.dbFileName, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        err = ''
        if 'INSERT' == sql[:6]:
            resData = getLastId(cursor)
        cursor.close()        
    except Exception as ex: 
        err = f"SQL eror:\n   {sql}\n   {ex.args[0]}\n   data = {data}"
    finally:
        if conn:
            conn.close()
    return err, resData


if __name__ == '__main__':
    create_db()

