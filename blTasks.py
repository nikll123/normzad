import dbTasks

def delete(id):
    err = dbTasks.delete(id)
    return err
    
def selectAll():
    err, data = dbTasks.select()
    return err, data

def getName(id):
    err, data = dbTasks.select(flds=['Name'],cond=f'id={id}')
    if not err:
        name = data[0][0]
    else:
        name = None
    return err, name

def updName(id, name):
    err = dbTasks.update(id, name)
    return err

def insName(name):
    err, newId = dbTasks.insert(name)
    return err, newId

