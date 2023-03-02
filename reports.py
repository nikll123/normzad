import dbCommon

def vJobs():
    err, data = dbCommon.select("vJobs")
    if not err:
        return data
    
# vJobs()
