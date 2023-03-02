import dbWorkers

def delete(id):
    err = dbWorkers.delete(id)
    return err
    
def selectAll():
    err, data = dbWorkers.select()
    return err, data

def selectFioNumAll():
    err, data = dbWorkers.selectFioNum()
    return err, data

# def getName(id):
#     err, data = dbWorkers.select(flds=['Name'],cond=f'id={id}')
#     if not err:
#         name = data[0][0]
#     else:
#         name = None
#     return err, name

# def updName(id, name):
#     err = dbWorkers.update(id, name)
#     return err

# def insName(name):
#     err, newId = dbWorkers.insert(name)
#     return err, newId

