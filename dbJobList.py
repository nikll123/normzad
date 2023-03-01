import dbCommon

tableName = "Jobs"
viewName = "JobList"

def select(flds=['*'], cond='', order=''):
    err, data = _select(viewName, flds, cond, order)
    return err, data

def selectJobs(flds=['*'], cond='', order=''):
    err, data = _select(tableName, flds, cond, order)
    return err, data

def _select(tableName, fldsList, cond, order):
    err, data = dbCommon.select(tableName=tableName, fldsList=fldsList, cond=cond, order=order)
    return err, data


if __name__ == "__main__":
    print(select())