# Tasks stuff
import dbDictionary

tableName = 'Tasks'
def insert(newName):
    err, newId = dbDictionary.insert(tableName, newName)
    return err, newId

def delete(Id):
    err = dbDictionary.delete(tableName, Id)
    return err

def update(id, newName):
    err = dbDictionary.update(tableName, id, newName)
    return err

def select (flds=['*'], cond='', order=''):
    err, data = dbDictionary.select(tableName, flds, cond, order=order)
    return err, data



if __name__ == '__main__':
    err, idTest = insert("Tasks Test")
    print (err, idTest)

    if idTest != None:
        err = update(idTest, "Tasks Test new name")
        print (err)

        err = delete(idTest)
        print (err)


