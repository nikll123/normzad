import dbJobList

def selectAll():
    err, data = dbJobList.select()
    return err, data

