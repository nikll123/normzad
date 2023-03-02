import datetime

dbFileName = "normzad.db"
dummyNum = -1
dummyErr = 'Unknown error'
fmtDateGui = '%d.%m.%Y'
fmtDateDb = '%Y-%m-%d'

def dateGui(date):
    date = date.strftime(fmtDateGui)
    return date

def dateDb(date):
    date = date.strftime(fmtDateDb)
    return date

def dateGuiToDb(txt):
    try:
        date = datetime.datetime.strptime(txt, fmtDateGui)
        date =dateDb(date)
    except:
        date = None
    return date
