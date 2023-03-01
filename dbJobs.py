import datetime
import dbCommon

tableName = "Jobs"

def new(WorkerId, TaskId, Date, TimeJob, Comment):
    fldsList = ['WorkerId', 'TaskId', 'Date', 'TimeJob', 'Comment']
    err, newId = dbCommon.insert(tableName, fldsList, [WorkerId, TaskId, Date, TimeJob, Comment])
    return err, newId

def delete(delId):
    err  = dbCommon.delete(tableName, delId)
    return err

def update(id, WorkerId, TaskId, Date, TimeJob, Comment):
    fldsList = ['WorkerId', 'TaskId', 'Date', 'TimeJob', 'Comment']
    data = [WorkerId, TaskId, Date, TimeJob, Comment]
    err = dbCommon.update(tableName, fldsList, data, id)
    return err

def select(flds=['*'], cond=''):
    err, data = dbCommon.select(tableName=tableName, fldsList=flds, cond=cond)
    return err, data


if __name__ == "__main__":

    WorkerId, TaskId, Date, TimeJob, Comment = 121, 3, datetime.datetime.now().date(), 8, 'comment test'
    err, testId = new(WorkerId, TaskId, Date, TimeJob, Comment)
    if err:
        print(err)
    
    WorkerId, TaskId, Date, TimeJob, Comment = 125, 2, datetime.datetime.now().date(), 5, 'comment test2'
    err =  update(testId, WorkerId, TaskId, Date, TimeJob, Comment)

    err =  delete(testId)



