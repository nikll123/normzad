import dbDepartments

def delete(id):
    err = dbDepartments.delete(id)
    return err

def selectAll():
    err, data = dbDepartments.select()
    return err, data

def getName(id):
    err, data = dbDepartments.select(flds=['Name'], cond=f'id={id}')
    if not err:
        name = data[0][0]
    else:
        name = None
    return err, name

