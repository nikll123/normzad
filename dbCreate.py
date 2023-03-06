# модуль создания с БД

import sqlite3 
import config
import os

def create_db():
    res = False
    if not os.path.exists('normzad.db'):
        txt = 'Создание базы данных'
        with sqlite3.connect(config.dbFileName,
                             detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn:
            cursor = conn.cursor()

            cursor.execute("""CREATE TABLE IF NOT EXISTS 
                                Config(
                                    id   integer PRIMARY KEY AUTOINCREMENT, 
                                    showId integer);
                                        """)
            cursor.execute("INSERT INTO Config (showId) VALUES (1);")

            cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    Departments(
                            id   integer PRIMARY KEY AUTOINCREMENT, 
                            Name text    NOT NULL);
                            """)
            cursor.execute("""CREATE UNIQUE INDEX IF NOT EXISTS 
                    indexUniqueDepartments 
                            ON Departments(Name);
                            """)

            #----------------------
            cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    Positions(
                            id   integer PRIMARY KEY AUTOINCREMENT, 
                            Name text    NOT NULL);
                            """)
            cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS indexUniquePositions ON Positions(Name);")

            #----------------------
            cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    Tasks(
                            id   integer PRIMARY KEY AUTOINCREMENT, 
                            Name text    NOT NULL);
                            """)
            cursor.execute("""CREATE UNIQUE INDEX IF NOT EXISTS 
                    indexUniqueTasks 
                            ON Tasks(Name);
                            """)

            #----------------------
            cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    Workers(
                            id           integer PRIMARY KEY AUTOINCREMENT, 
                            TabNum       integer NOT NULL, 
                            LastName     text    NOT NULL, 
                            Name         text    NOT NULL, 
                            SecondName   text    NOT NULL,
                            PositionId   integer NOT NULL,
                            Level        integer NOT NULL,
                            DepartmentId integer NOT NULL,
                            FOREIGN KEY(DepartmentId) REFERENCES Departments(id),
                            FOREIGN KEY(PositionId) REFERENCES Positions(id));
                            """)
            
            cursor.execute("""CREATE UNIQUE INDEX IF NOT EXISTS 
                    indexworkers 
                            ON workers(id);
                            """)
            cursor.execute("""CREATE UNIQUE INDEX IF NOT EXISTS 
                    indexworkersTabNum 
                            ON workers(TabNum);
                            """)

            #----------------------
            cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    Jobs(
                        id           integer   PRIMARY KEY AUTOINCREMENT,
                        WorkerId     integer   NOT NULL, 
                        TaskId       integer   NOT NULL, 
                        Date         date      NOT NULL, 
                        TimeJob      integer   NOT NULL,
                        Comment      text      NOT NULL,
                        FOREIGN KEY(WorkerId) REFERENCES Workers(id),
                        FOREIGN KEY(TaskId) REFERENCES Tasks(id));
                        """)

            cursor.execute("""CREATE VIEW IF NOT EXISTS 
                    vJobs
                        AS 
                        SELECT  
                            j.id, 
                            j.WorkerId, 
                            j.TaskId, 
                            strftime('%d.%m.%Y', j.Date) as Date,
                            w.TabNum,
                            w.FIO,
                            w.Level, 
                            p.Name AS Position, 
                            t.Name AS Task, 
                            j.TimeJob,
                            j.Comment,
                            d.Name AS Department
                        FROM    
                            Jobs        AS j, 
                            Tasks       AS t,
                            vWorkers    AS w,
                            Positions   AS p,
                            Departments AS d
                        WHERE   
                            j.TaskId = t.id     AND
                            j.WorkerId = w.id   AND
                            w.PositionId = p.id AND
                            w.DepartmentId = d.id
                        ORDER BY 
                            j.Date,
                            j.WorkerId
                            """)      

            cursor.execute("""CREATE VIEW IF NOT EXISTS 
                    vWorkerFio
                        AS 
                        SELECT id,
                                LastName || ' ' || SUBSTR(Name,1,1) || '. ' || SUBSTR(SecondName,1,1) || '.' AS FIO 
                        FROM 
                                workers
                        ORDER BY 
                                FIO
                            """)
        

            cursor.execute("""CREATE VIEW IF NOT EXISTS 
                    vWorkers
                        AS 
                        SELECT 
                                w.id, 
                                w.TabNum, 
                                w.LastName, 
                                w.Name, 
                                w.SecondName, 
                                w.Level, 
                                d.Name as Department, 
                                p.Name as Position,
                                w.DepartmentId, 
                                w.PositionId,
                                wfio.FIO,
                                wfio.FIO || '  (' || w.TabNum || ')' as FIO_Num
                        FROM 
                                Workers as w, 
                                vWorkerFio as wfio, 
                                Departments as d, 
                                Positions as p
                        WHERE 
                                    w.id = wfio.id 
                                AND w.DepartmentId = d.id 
                                AND w.PositionId = p.id
                        ORDER BY 
                                FIO;
                            """)
            res = True
    else:
        txt = "Файл уже существует"
    print (txt)
    return res


if __name__ == '__main__':
    if create_db():
        import dbTestData
    

