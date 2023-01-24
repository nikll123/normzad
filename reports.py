import db

def JobList():
    err, data = db.select("jobList")
    if not err:
        print(data)
    
JobList()
