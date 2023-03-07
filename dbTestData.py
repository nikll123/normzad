import dbCommon

def testData():
    print('Внесение тестовых данных')
    tableName = 'Departments'
    fldList = ['name']
    for d in ['СТО цех эксплуатации'], ['ЧПМ']:
        err, newId = dbCommon.insert(tableName,fldList,d)
        if err:
            print (err)

    tableName = 'Positions'
    fldList = ['name']
    for d in ['Дворник'], ['ЧПМ'], ['Кочегар'], ['Машинист'], ['Электрик'], ['Начальник']:
        err, newId = dbCommon.insert(tableName,fldList,d)
        if err:
            print (err)

    tableName = 'Tasks'
    fldList = ['name']
    for d in ['Снегоборьба'],['Репонт плат КТПЦ'],['Ремонт ПСС'],['Командировка'],['Отпуск'],['Больничный'],['Управление паровозом']:
        err, newId = dbCommon.insert(tableName,fldList,d)
        if err:
            print (err)


    import random
    def randomId(tableName):
        fldList = ['id']
        err, ids = dbCommon.select(tableName,fldList, cond='',order='')
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
    # fldList = ['id','LastName','Name','SecondName','PositionId','Level', 'DepartmentId']
    # workerList = []
    # workerList.append([121, 'Иванов',  'Иван',  'Иванович',    rndPosId(),rndLev(),rndDepId()])
    # workerList.append([125, 'Петров',  'Петр',  'Петрович',    rndPosId(),rndLev(),rndDepId()])
    # workerList.append([136, 'Сидоров', 'Сидор', 'Сидорович',   rndPosId(),rndLev(),rndDepId()])
    # workerList.append([157, 'Попова',  'Мария', 'Спиридоновна',rndPosId(),rndLev(),rndDepId()])
    # workerList.append([150, 'Джонсон', 'Джон',  'Джонович',    rndPosId(),rndLev(),rndDepId()])

    fldList = ['TabNum', 'LastName','Name','SecondName','PositionId','Level', 'DepartmentId']
    workerList = []
    workerList.append([156,'Иванов',  'Иван',  'Иванович',    rndPosId(),rndLev(),rndDepId()])
    workerList.append([258,'Петров',  'Петр',  'Петрович',    rndPosId(),rndLev(),rndDepId()])
    workerList.append([452,'Сидоров', 'Сидор', 'Сидорович',   rndPosId(),rndLev(),rndDepId()])
    workerList.append([112,'Попова',  'Мария', 'Спиридоновна',rndPosId(),rndLev(),rndDepId()])
    workerList.append([12355,'Джонсон', 'Джон',  'Джонович',    rndPosId(),rndLev(),rndDepId()])

    for wd in workerList:
        err, newId = dbCommon.insert(tableName,fldList,wd)
        if err:
            print (err)

    def rndTabNom():
        return randomId('Workers')

    def rndTaskId():
        return randomId('Tasks')

    def rndTime():
        return random.randrange(4, 9)

    tableName = 'Jobs'
    fldList = ['WorkerId', 'TaskId', 'Date', 'TimeJob', 'Comment']
    jobsList = []

    date = dbCommon.dateToDbFormat('22.01.2023')
    for i in range(5):
        jobsList.append([rndTabNom(), rndTaskId(), date, rndTime(), f'comment {random.randrange(0, 1000)}'])

    date = dbCommon.dateToDbFormat('23.1.2023')
    for i in range(4):
        jobsList.append([rndTabNom(), rndTaskId(), date, rndTime(), f'comment {random.randrange(0, 1000)}'])

    date = dbCommon.dateToDbFormat('24.1.2023')
    for i in range(5):
        jobsList.append([rndTabNom(), rndTaskId(), date, rndTime(), f'comment {random.randrange(0, 1000)}'])

    for jd in jobsList:
        err, newId = dbCommon.insert(tableName, fldList, jd)
        if err:
            print (err)

