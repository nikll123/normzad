import dbJobList

def selectAll():
    err, data = dbJobList.select()
    return err, data

def getJobListRow(id):
    err, data = dbJobList.select(cond=f'id={id}')
    return err, data
