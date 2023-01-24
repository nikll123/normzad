import db

# Внесение тестовых данных
tableName = 'Departments'
fldList = ['name']
for d in ['СТО цех эксплуатации'], ['ЧПМ']:
    err, newId = db.insert(tableName,fldList,d)
    if err:
        print (err)

tableName = 'Positions'
fldList = ['name']
for d in ['Дворник'], ['ЧПМ'], ['Кочегар'], ['Машинист'], ['Электрик'], ['Начальник']:
    err, newId = db.insert(tableName,fldList,d)
    if err:
        print (err)

tableName = 'Tasks'
fldList = ['name']
for d in ['Снегоборьба'],['Репонт плат КТПЦ'],['Ремонт ПСС'],['Командировка'],['Отпуск'],['Больничный'],['Управление паровозом']:
    err, newId = db.insert(tableName,fldList,d)
    if err:
        print (err)


import random
def randomId(tableName, fldId='id'):
    fldList = [fldId]
    err, ids = db.select(tableName,fldList)
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
    err, newId = db.insert(tableName,fldList,wd)
    if err:
        print (err)

import datetime
def rndTabNom():
    return randomId('Workers', fldId='TabelNom')

def rndTaskId():
    return randomId('Tasks')

def rndTime():
    return random.randrange(4, 9)

tableName = 'Jobs'
fldList = ['TabelNom', 'TaskId', 'Date', 'TimeJob', 'Comment']
jobsList = []
for i in range(5):
    jobsList.append([rndTabNom(), rndTaskId(), datetime.date(2023,1,22), rndTime(), f'comment {random.randrange(0, 1000)}'])

for i in range(4):
    jobsList.append([rndTabNom(), rndTaskId(), datetime.date(2023,1,23), rndTime(), f'comment {random.randrange(0, 1000)}'])

for i in range(5):
    jobsList.append([rndTabNom(), rndTaskId(), datetime.date(2023,1,24), rndTime(), f'comment {random.randrange(0, 1000)}'])

for jd in jobsList:
    err, newId = db.insert(tableName, fldList, jd)
    if err:
        print (err)

