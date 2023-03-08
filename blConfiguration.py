import os
import dbConfiguration, config, guiCommon

def getShowId():
    err, showId = dbConfiguration.getShowId()
    return err, showId

def setShowId(val):   # val: 0 or 1
    res = dbConfiguration.setShowId(val)
    return res

def createDB():
    import dbCreate
    err, res = dbCreate.create_db()
    return err, res

def createTestData():
    import dbTestData
    dbTestData.testData()

def checkConfig():
    err = ''
    if not os.path.exists(config.dbFileName):   # создать БД если ее нет
        err, res = createDB()
    
    if guiCommon.notError(err):
        if not os.path.exists(config.reportsDir):   # если нет папки для отчетов - то создать ее
            os.makedirs(config.reportsDir)


if __name__ == '__main__':
    print(getShowId())
    print(setShowId(False))
    print(getShowId())
    print(setShowId(True))
    print(getShowId())
