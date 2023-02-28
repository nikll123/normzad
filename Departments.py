import dbDepartments

def delete(id):
    err = dbDepartments.delete(id)
    return err

def selectAll():
    err, data = dbDepartments.select()
    return err, data

def getName(id):
    cond = f'id={id}'
    err, data = dbDepartments.select(flds=['Name'], cond=cond)
    name = None
    if not err:
        if len(data) ==0:
            err = f'{cond}: Не найдено'
        else:
            name = data[0][0]
    return err, name

def updName(id, name):
    err = dbDepartments.update(id, name)
    return err

def insName(name):
    err, newId = dbDepartments.new(name)
    return err, newId

