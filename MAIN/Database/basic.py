import sqlite3

connection=sqlite3.connect('example.db')
cursor=connection.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS PERSON(
    first_name TEXT,
    last_name TEXT,
    age INTEGER
    )
    """
)
connection.commit()

cursor.execute(
    """
    INSERT INTO PERSON VALUES 
    ("SA","LA",65),
    ("MA","FA",55)
    """
)

cursor.execute(
    """
    SELECT * FROM PERSON WHERE
    age=65
    """
)
result=cursor.fetchall()
print(result)
cursor.execute(
    """
    SELECT * FROM PERSON
    """
)
result=cursor.fetchall()
print(result)

connection.close()