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

def select(tableName, fldsList, cond=''):
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

    # Внесение тестовых данных
    tableName = 'Departments'
    fldList = ['name']
    for d in ['СТО цех эксплуатации'], ['ЧПМ']:
        err, newId = insert(tableName,fldList,d)
        if err:
            print (err)
    
    tableName = 'Positions'
    fldList = ['name']
    for d in ['Дворник'], ['ЧПМ'], ['Кочегар'], ['Машинист'], ['Электрик'], ['Начальник']:
        err, newId = insert(tableName,fldList,d)
        if err:
            print (err)

    tableName = 'Tasks'
    fldList = ['name']
    for d in ['Снегоборьба'],['Репонт плат КТПЦ'],['Ремонт ПСС'],['Командировка'],['Отпуск'],['Больничный'],['Управление паровозом']:
        err, newId = insert(tableName,fldList,d)
        if err:
            print (err)

  
    import random
    def randomId(tableName):
        fldList = ['id']
        err, ids = select(tableName,fldList)
        randomIx = random.randrange(0, len(ids))
        rndId = ids[randomIx][0]
        return rndId

    def rndPosId():
        return randomId('Positions')
    def rndDepId():
        return randomId('Departments')
    def rndLev():
        return random.randrange(1, 10)


    tableName = 'Workers'
    fldList = ['TabelNom','LastName','Name','SecondName','PositionId','Level', 'DepartmentId']
    workerList = []
    workerList.append([121, 'Иванов',  'Иван',  'Иванович',    rndPosId(),rndLev(),rndDepId()])
    workerList.append([125, 'Петров',  'Петр',  'Петрович',    rndPosId(),rndLev(),rndDepId()])
    workerList.append([136, 'Сидоров', 'Сидор', 'Сидорович',   rndPosId(),rndLev(),rndDepId()])
    workerList.append([157, 'Попова',  'Мария', 'Спиридоновна',rndPosId(),rndLev(),rndDepId()])
    workerList.append([150, 'Джонсон', 'Джон',  'Джонович',    rndPosId(),rndLev(),rndDepId()])
    
    for wd in workerList:
        err, newId = insert(tableName,fldList,wd)
        if err:
            print (err)
    
