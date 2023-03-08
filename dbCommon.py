import sqlite3 
import datetime
import config
import os
from collections import namedtuple

def getLastId(cursor):
    res = cursor.execute("Select last_insert_rowid()")
    return res.lastrowid
    
def namedtuple_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    cls = namedtuple("Row", fields)
    return cls._make(row)

def execute(sql, params=[]):
    err = config.dummyErr
    data = None
    if os.path.exists(config.dbFileName):
        with sqlite3.connect(config.dbFileName, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn:
            # conn.row_factory = sqlite3.Row
            conn.row_factory = namedtuple_factory  # row.field
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
    else:
        err = f'Нет файла: {config.dbFileName}'
    return err, data


# Эта функция (executeTry) - полный аналог функции execute, но без использования команды with 
def executeTry(sql, data=[]):
    err = config.dummyErr
    newId = None
    try:
        conn = sqlite3.connect(config.dbFileName, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES, )
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

def delete(tableName, id):
    sql = f"DELETE FROM {tableName} WHERE id=?"
    err, _notUsed = execute(sql, [id])
    return err

def update(tableName, fldsList, data, id):
    list = []
    for f in fldsList:
        list.append(f'{f}=?')
    substr = ','.join(list)
    sql = f"UPDATE {tableName} SET {substr} WHERE id=?"
    data.append(id)
    err, _notUsed = execute(sql, data)
    return err

def select(tableName, fldsList, cond, order):
    substr = ','.join(fldsList)
    if cond:
        where = f"WHERE {cond}"
    else:
        where = ''
    if order:
        orderby = f"ORDER BY {order}"
    else:
        orderby = ''

    sql = f"SELECT {substr} FROM {tableName} {where} {orderby}"
    err, data = execute(sql)
    return err, data

# def dateGui(date):
#     date = date.strftime(config.fmtDateGui)
#     return date

# def dateDb(date):
#     date = date.strftime(config.fmtDateDb)
#     return date

def dateToDbFormat(txt):
    try:
        date = datetime.datetime.strptime(txt, config.fmtDateGui)
        date = date.strftime(config.fmtDateDb)
        # date =dateDb(date)
    except:
        date = None
    return date

if __name__ == '__main__':
    sql = 'select * from table'
    err, data = execute(sql)
    print(err)