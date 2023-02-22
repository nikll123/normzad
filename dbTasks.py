# Tasks stuff
import db

tableName = 'Tasks'
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
    err = db.delete(tableName, id)
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
    err, idTest = new("Tasks Test")
    print (err, idTest)

    if idTest != None:
        err = update(idTest, "Tasks Test new name")
        print (err)

        err = delete(idTest)
        print (err)


