# create a class DATABASE2
# and add a table students
# store the following details
# name, age, class, gender
# then create methods for
# adding, removing, view and searching
# student by name
# YAY

import sqlite3

class Database:

    table = 'Student'

    def __init__(self, name = 'sqlite3.databse'):
        self.con = sqlite3.connect(name)
        print('Connected')

    def run(self, query):
        try:
            self.con.execute(query)
            self.con.commit()
            return True
        except Exception as e:
            print(query)
            print(e)
            return False
        
    def create_table(self):
        query = f"""
            CREATE TABLE {self.table} (
                roll_no INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                class TEXT,
                gender TEXT
            )
        """

        return self.run(query)

    def add(self, name, age, cls, gender):
        query = f"""
            INSERT INTO {self.table} VALUES(
                null, '{name}', {age}, '{cls}', '{gender}'
            )
        """
    
        return self.run(query)

    def remove(self, roll_no):
        query = f"DELETE FROM {self.table} WHERE roll_no = {roll_no}"

        return self.run(query)

    def search(self, name):
        query = f"SELECT * FROM {self.table} WHERE name = '{name}'"

        return self.view(query)

    def viewall(self):
        query = f"SELECT * FROM {self.table}"

        return self.view(query)

    def view(self, query):
        try:
            result = self.con.execute(query)
            return result.fetchall()
        except Exception as e:
            print('Error')
            print(e)