import dbCommon

tableName = "Jobs"
viewName = "vJobs"

def selectView(flds=['*'], cond='', order=''):
    err, data = _select(viewName, flds, cond, order)
    return err, data

def select(flds=['*'], cond='', order=''):
    err, data = _select(tableName, flds, cond, order)
    return err, data

def insert(WorkerId,TaskId,Date,TimeJob,Comment):
    flds = ['WorkerId','TaskId','Date','TimeJob','Comment']
    data = [WorkerId,TaskId,Date,TimeJob,Comment]
    err, newId = dbCommon.insert(tableName=tableName, fldsList=flds,data=data)
    return err, newId

def delete(id):
    err = dbCommon.delete(tableName=tableName,id=id)
    return err

def update(id, data, flds=['WorkerId','TaskId','Date','TimeJob','Comment']):
    err = dbCommon.update(tableName=tableName, fldsList=flds,data=data)
    return err

def _select(tableName, fldsList, cond, order):
    err, data = dbCommon.select(tableName=tableName, fldsList=fldsList, cond=cond, order=order)
    return err, data


if __name__ == "__main__":
    print(selectView())