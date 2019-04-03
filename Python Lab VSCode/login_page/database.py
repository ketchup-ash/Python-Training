import sqlite3

class Database:
    table = 'Data'

    def __init__(self, name = 'sqlite3.database'):
        con = sqlite3.connect(name)
        

    def run(self, query):
        try:


query = f"CREATE TABLE {self.table} (
            id TEXT,
            password TEXT
        )"

        return self.run(query)