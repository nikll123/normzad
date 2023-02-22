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
        sql = "CREATE UNIQUE INDEX IF NOT EXISTS indexUniqueDepartments ON Departments(Name);"
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS Positions(
                    id   integer PRIMARY KEY AUTOINCREMENT, 
                    Name text    NOT NULL
                    );"""
        cursor.execute(sql)
        sql = """CREATE UNIQUE INDEX IF NOT EXISTS indexUniquePositions ON Positions(Name);"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS Tasks(
                    id   integer PRIMARY KEY AUTOINCREMENT, 
                    Name text    NOT NULL
                    );"""
        cursor.execute(sql)
        sql = "CREATE UNIQUE INDEX IF NOT EXISTS indexUniqueTasks ON Tasks(Name);"
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS workers(
                    id           integer PRIMARY KEY AUTOINCREMENT, 
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
        sql = "CREATE UNIQUE INDEX IF NOT EXISTS indexworkers ON workers(id);"
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS jobs(
                    id           integer   PRIMARY KEY AUTOINCREMENT,
                    WorkerId     integer   NOT NULL, 
                    TaskId       integer   NOT NULL, 
                    Date         date      NOT NULL, 
                    TimeJob      integer   NOT NULL,
                    Comment      text      NOT NULL,
                    FOREIGN KEY(WorkerId) REFERENCES Workers(id),
                    FOREIGN KEY(TaskId) REFERENCES Tasks(id)
                    );"""
        cursor.execute(sql)

        sql = """CREATE VIEW IF NOT EXISTS jobList
                    AS 
                    SELECT  
                            j.id, 
                            j.Date, 
                            j.WorkerId, 
                            w.LastName || ' ' || SUBSTR(w.Name,1,1) || '. ' || SUBSTR(w.SecondName,1,1) || '.' AS shortName,
                            w.Level, 
                            p.Name AS Position, 
                            t.Name AS Task, j.TimeJob
                    FROM    
                            jobs      AS j, 
                            Tasks     AS t,
                            Workers   AS w,
                            Positions AS p
                    WHERE   
                            j.TaskId = t.id    AND
                            j.WorkerId = w.id  AND
                            w.Positionid = p.id
                    ORDER BY 
                            j.Date,
                            j.WorkerId
                    ;"""        
        cursor.execute(sql)

        sql = """CREATE VIEW IF NOT EXISTS workerList
                    AS 
                    SELECT 
                            w.id, 
                            w.LastName, 
                            w.Name, 
                            w.SecondName, 
                            w.Level, 
                            d.Name as Department, 
                            p.Name as position,
                            DepartmentId, 
                            PositionId
                    FROM 
                            workers as w, 
                            Departments as d, 
                            Positions as p
                    WHERE 
                            w.DepartmentId = d.id 
                            AND w.PositionId = p.id
                    ORDER BY 
                            w.LastName, 
                            w.Name, 
                            w.SecondName
                    ;"""
        cursor.execute(sql)

        sql = """CREATE VIEW IF NOT EXISTS vPositions
                        AS 
                        SELECT 
                            id,
                            Name
                        FROM Positions 
                        ORDER BY Name
                        ;"""
        cursor.execute(sql)
            
        sql = """CREATE VIEW IF NOT EXISTS vDepartments
                        AS 
                        SELECT 
                            id,
                            Name
                        FROM Departments
                        ORDER BY Name
                        ;"""
        cursor.execute(sql)
            


def getLastId(cursor):
    res = cursor.execute("Select last_insert_rowid()")
    res = res.fetchone()
    return res[0]

def execute(sql, params=[]):
    err = config.dummyErr
    data = None
    with sqlite3.connect(config.dbFileName, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        try:
            cursor.execute(sql, params)
            err = ''
            if 'INSERT' == sql[:6]:
                data = getLastId(cursor)
            elif 'SELECT' == sql[:6]:
                data = cursor.fetchall()
        except Exception as ex: 
            err = f"SQL eror:\n   {sql}\n   {ex.args[0]}\n   data = {params}"
    return err, data

# Эта функция (executeTry) - полный аналог функции execute, но без использования команды with 
def executeTry(sql, data=[]):
    err = config.dummyErr
    newId = None
    try:
        conn = sqlite3.connect(config.dbFileName, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql, data)
        conn.commit()
        err = ''
        if 'INSERT' == sql[:6]:
            newId = getLastId(cursor)
        cursor.close()        
    except Exception as ex: 
        err = f"SQL eror:\n   {sql}\n   {ex.args[0]}\n   data = {data}"
    finally:
        if conn:
            conn.close()
    return err, newId

def insert(tableName, fldsList, data):
    fldsText = ','.join(fldsList)
    placeHolders = []
    for f in fldsList:
        placeHolders.append('?')
    placeHoldersText = ','.join(placeHolders)
    sql = f"INSERT INTO {tableName} ({fldsText}) VALUES ({placeHoldersText});"
    err, newId = execute(sql, data)
    return err, newId 

def delete(tableName, fldPK, id):
    sql = f"DELETE FROM {tableName} WHERE {fldPK}=?"
    err, _notUsed = execute(sql, [id])
    return err

def update(tableName, fldsList, data, fldPK, id):
    list = []
    for f in fldsList:
        list.append(f'{f}=?')
    substr = ','.join(list)
    sql = f"UPDATE {tableName} SET {substr} WHERE {fldPK}=?"
    data.append(id)
    err, _notUsed = execute(sql, data)
    return err

def select(tableName, fldsList=["*"], cond=''):
    substr = ','.join(fldsList)
    if cond:
        where = f"WHERE {cond}"
    else:
        where = ''
    sql = f"SELECT {substr} FROM {tableName} {where}"
    err, data = execute(sql)
    return err, data

if __name__ == '__main__':
    # Создание базы данных
    create_db()

    import dbTestData
    

