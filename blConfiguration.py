import dbConfiguration

def getShowId():
    err, showId = dbConfiguration.getShowId()
    return err, showId

def setShowId(val):   # val: 0 or 1
    res = dbConfiguration.setShowId(val)
    return res
    
if __name__ == '__main__':
    print(getShowId())
    print(setShowId(False))
    print(getShowId())
    print(setShowId(True))
    print(getShowId())
