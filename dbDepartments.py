# deparments stuff
import dbDictionary

tableName = 'Departments'
def insert(newName):
    err, newId = dbDictionary.insert(tableName, newName)
    return err, newId

def delete(Id):
    err = dbDictionary.delete(tableName, Id)
    return err

def update(id, newName):
    err = dbDictionary.update(tableName, id, newName)
    return err

def select (flds=['*'], cond='',order=''):
    err, data = dbDictionary.select(tableName, flds, cond, order)
    return err, data


if __name__ == '__main__':
    err, idTest = insert("dept Test")
    print (err, idTest)

    if idTest != None:
        err = update(idTest, "dept Test new name")
        print (err)

        err = delete(idTest)
        print (err)
