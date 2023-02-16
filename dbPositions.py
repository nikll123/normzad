# Positions stuff
import db

tableName = 'Positions'
pkField = 'id'

def new(newName):
    newName = newName.strip()
    if newName:
        fldList = ['Name']
        err, newId  = db.insert(tableName, fldList, [newName])
    else:
        newId = None
        err = "Нет данных"
    return err, newId

def delete(id):
    err = db.delete(tableName, pkField, id)
    return err

def update(id, newName):
    newName = newName.strip()
    if newName:
        fldList = ['Name']
        err = db.update(tableName, fldList, [newName], pkField, id)
    else:
        err = "Нет данных"
    return err


if __name__ == '__main__':
    err, idTest = new("position Test")
    print (err, idTest)

    if idTest != None:
        err = update(idTest, "position Test new name")
        print (err)

        err = delete(idTest)
        print (err)


