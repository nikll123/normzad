import dbCommon

tableName = "JobList"

def select(flds=['*'], cond=''):
    err, data = dbCommon.select(tableName=tableName, fldsList=flds, cond=cond)
    return err, data

if __name__ == "__main__":
    print(select())