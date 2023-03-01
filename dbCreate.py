# модуль создания с БД

import sqlite3 
import config

def create_db():
    print('Создание базы данных')
    with sqlite3.connect(config.dbFileName, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn:
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
                Departments(
                        id   integer PRIMARY KEY AUTOINCREMENT, 
                        Name text    NOT NULL);
                        """)
        cursor.execute("""CREATE UNIQUE INDEX IF NOT EXISTS 
                indexUniqueDepartments 
                        ON Departments(Name);
                        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
                Positions(
                        id   integer PRIMARY KEY AUTOINCREMENT, 
                        Name text    NOT NULL);
                        """)
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS indexUniquePositions ON Positions(Name);")

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
                Tasks(
                        id   integer PRIMARY KEY AUTOINCREMENT, 
                        Name text    NOT NULL);
                        """)
        cursor.execute("""CREATE UNIQUE INDEX IF NOT EXISTS 
                indexUniqueTasks 
                        ON Tasks(Name);
                        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
                workers(
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

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
                jobs(
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
                jobList
                    AS 
                    SELECT  
                            j.id, 
                            j.Date, 
                            w.TabNum, 
                            w.LastName || ' ' || SUBSTR(w.Name,1,1) || '. ' || SUBSTR(w.SecondName,1,1) || '.' AS shortName,
                            w.Level, 
                            p.Name AS Position, 
                            t.Name AS Task, 
                            j.TimeJob
                    FROM    
                            jobs      AS j, 
                            Tasks     AS t,
                            Workers   AS w,
                            Positions AS p
                    WHERE   
                            j.TaskId = t.id    AND
                            j.WorkerId = w.id  AND
                            w.Positionid = p.id
                    ORDER BY 
                            j.Date,
                            j.WorkerId;
                            """)      

        cursor.execute("""CREATE VIEW IF NOT EXISTS 
                vWorkers
                    AS 
                    SELECT *,
                            LastName || ' ' || SUBSTR(Name,1,1) || '. ' || SUBSTR(SecondName,1,1) || '.' AS FIO 
                    FROM 
                            workers
                    ORDER BY 
                            FIO
                        """)
       

        cursor.execute("""CREATE VIEW IF NOT EXISTS 
                workerList
                    AS 
                    SELECT 
                            w.id, 
                            w.TabNum, 
                            w.LastName, 
                            w.Name, 
                            w.SecondName, 
                            w.Level, 
                            d.Name as Department, 
                            p.Name as position,
                            w.DepartmentId, 
                            w.PositionId,
                            w.FIO,
                            w.FIO || '  (' || w.TabNum || ')' as FIO_Num
                    FROM 
                            vWorkers as w, 
                            Departments as d, 
                            Positions as p
                    WHERE 
                            w.DepartmentId = d.id 
                            AND w.PositionId = p.id
                    ORDER BY 
                            FIO;
                        """)


if __name__ == '__main__':
    create_db()
    import dbTestData
    

