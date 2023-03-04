import dbCommon

def rJobs():
    err, data = dbCommon.select("vJobs")
    if not err:
        return data
    
# vJobs()
