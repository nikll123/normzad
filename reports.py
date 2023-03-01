import dbCommon

def JobList():
    err, data = dbCommon.select("jobList")
    if not err:
        return data
    
# JobList()
