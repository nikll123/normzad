import dbJobs
import config

def selectAll():
    err, data = dbJobs.selectView()
    for ix in range(len(data)):
        date = config.dateGui(data[ix].Date)
        data[ix].Date = date
    return err, data

def getJobListRow(id):
    err, data = dbJobs.selectView(cond=f'id={id}')
    return err, data

def get(id):
    err, data = dbJobs.select(cond=f'id={id}')
    return err, data

def add(date, timeJob, taskId, workerId, comment):
    err, newId = dbJobs.insert(workerId,taskId,date,timeJob,comment)
    return err, newId

def save(id, date, timeJob, taskId, workerId, comment):
    err = dbJobs(id,workerId,taskId,date,timeJob,comment)
    return err
