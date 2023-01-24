import datetime
import db

tableName = "Jobs"

def new(TabelNom, TaskId, Date, TimeJob, Comment):
    fldsList = ['TabelNom', 'TaskId', 'Date', 'TimeJob', 'Comment']
    err, newId = db.insert(tableName, fldsList, [TabelNom, TaskId, Date, TimeJob, Comment])
    return err, newId

def delete(delId):
    err  = db.delete(tableName, 'id', delId)
    return err

def update(id, TabelNom, TaskId, Date, TimeJob, Comment):
    fldsList = ['TabelNom', 'TaskId', 'Date', 'TimeJob', 'Comment']
    err = db.update(tableName, fldsList, [TabelNom, TaskId, Date, TimeJob, Comment],'id', id)
    return err


if __name__ == "__main__":

    TabelNom, TaskId, Date, TimeJob, Comment = 121, 3, datetime.datetime.now().date(), 8, 'comment test'
    err, testId = new(TabelNom, TaskId, Date, TimeJob, Comment)
    if err:
        print(err)
    
    TabelNom, TaskId, Date, TimeJob, Comment = 125, 2, datetime.datetime.now().date(), 5, 'comment test2'
    err =  update(testId, TabelNom, TaskId, Date, TimeJob, Comment)

    err =  delete(testId)


