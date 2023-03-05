import dbJobs

def selectAll():
    err, data = dbJobs.selectView2()
    return err, data

# def getJobListRow(id):
#     err, data = dbJobs.selectView(cond=f'id={id}')
#     return err, data

def get(id):
    res = None
    err, data = dbJobs.selectView2(cond=f'id={id}')
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