import dbJobs

def selectAll():
    err, data = dbJobs.selectView()
    return err, data

def select(flds):
    err, data = dbJobs.selectView(flds)
    return err, data

def getJobListRow(id):
    res = None
    err, data = dbJobs.selectView(cond=f'id={id}')
    if not err:
        res = data[0]
    return err, res

def get(id):
    res = None
    err, data = dbJobs.selectView(cond=f'id={id}')
    if not err:
        res = data[0]
    return err, res

def add(date, timeJob, taskId, workerId, comment):
    err, newId = dbJobs.insert(workerId,taskId,date,timeJob,comment)
    return err, newId

def save(id, date, timeJob, taskId, workerId, comment):
    err = dbJobs.update(id,[workerId,taskId,date,timeJob,comment])
    return err

def delete(id):
    err = dbJobs.delete(id)
    return err