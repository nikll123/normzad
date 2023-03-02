import sqlite3
import config

conn = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS d(d  date NOT NULL)")
d = config.dateGuiToDb('01.05.2020')
sql = f"insert into d (d) values('{d}')"
cursor.execute(sql)
cursor.execute("select * from d")
data = cursor.fetchall()
d = config.dateDb(data[0][0])
print(d)
d = config.dateGui(data[0][0])
print(d)

print(config.dateGuiToDb(d))
print(config.dateGuiToDb('50.60.30'))

pass
