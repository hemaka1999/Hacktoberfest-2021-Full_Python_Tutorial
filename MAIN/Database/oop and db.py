import sqlite3

class Person:
    def __init__(self,id=-1,first_name="",second_name="",age=-1):
        self.id=id
        self.first_name=first_name
        self.second_name=second_name
        self.age=age
        self.connection = sqlite3.connect('example2.db')
        self.cursor = connection.cursor()


    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS PERSON(
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER
            )
            """
        )

    def insert_data(self):
        self.cursor.execute(
            f"""
            INSERT INTO PERSON VALUES
            ({self.id},'{self.first_name}','{self.second_name}',{self.age})
            """
        )
        self.connection.commit()




    def load_data(self,id):
        cursor.execute(f"""
        SELECT * FROM PERSON WHERE
        id={id}
        """)
        result=cursor.fetchone()
        self.id=id
        self.first_name=result[1]
        self.second_name=result[2]
        self.age=result[3]

        x=cursor.execute("""
        SELECT * FROM PERSON
        """)
        print(x.fetchall())
        self.result_all=cursor.fetchall()





connection=sqlite3.connect('example2.db')
cursor=connection.cursor()
p1=Person(1,"mk","sd",56)
p1.create_table()
p1.insert_data()
p1.load_data(1)
print(p1.id)
print(p1.first_name)



connection.close()