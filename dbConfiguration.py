import dbCommon

def getShowId():
    showId = None
    err, data = dbCommon.select(tableName='Config', fldsList=['showId'],cond='id=1',order='')
    if not err:
        showId = data[0].showId 
    return err, showId

def setShowId(newVal):
    err = dbCommon.update(tableName='Config', fldsList=['showId'], data=[newVal], id=1)
    return err

if __name__ == '__main__':
    print(getShowId())
    setShowId(0)
    print(getShowId())
    setShowId(1)
    print(getShowId())

