import dbWorkers

def delete(id):
    err = dbWorkers.delete(id)
    return err
    
def selectAll():
    err, data = dbWorkers.select()
    return err, data

def select(flds):
    err, data = dbWorkers.select(flds=flds)
    return err, data

def selectFioNumAll():
    err, data = dbWorkers.selectFioNum()
    return err, data

def get(id):
    res = None
    err, data = dbWorkers.select(cond=f'id={id}')
    if not err:
        res = data[0]
    return err, res

def add(tn,LastName,Name,SecondName,Level,PositionId,DepartmentId):
    err, LastName, Name, SecondName= _checkNames(LastName,Name,SecondName)
    if not err:
        err, newId = dbWorkers.insert(tn, LastName, Name, SecondName, Level, PositionId, DepartmentId)
    return err, newId
    
def save(id,tn,LastName,Name,SecondName,Level,PositionId,DepartmentId):
    err, LastName, Name, SecondName= _checkNames(LastName,Name,SecondName)
    if not err:
        err = dbWorkers.update(id, tn, LastName, Name, SecondName, Level, PositionId, DepartmentId)
    return err


def _checkNames(LastName,Name,SecondName):
    LastName = LastName.strip()
    Name = Name.strip()
    SecondName = SecondName.strip()
    if LastName and Name and SecondName:
        err = ''
    else:
        err = "Нет полного имени"
    return err, LastName, Name, SecondName
