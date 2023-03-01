import dbCommon

tableName = "JobList"

def select(flds=['*'], cond='', order=''):
    err, data = dbCommon.select(tableName=tableName, fldsList=flds, cond=cond, order=order)
    return err, data

if __name__ == "__main__":
    print(select())