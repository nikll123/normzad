import dbPositions

def delete(id):
    err = dbPositions.delete(id)
    return err
    
def selectAll():
    err, data = dbPositions.select()
    return err, data

def getName(id):
    err, data = dbPositions.select(flds=['Name'],cond=f'id={id}')
    if not err:
        name = data[0][0]
    else:
        name = None
    return err, name

def updName(id, name):
    err = dbPositions.update(id, name)
    return err

def insName(name):
    err, newId = dbPositions.new(name)
    return err, newId

