from homework2 import Database

db = Database()

# db.create_table()
# db.add('Prashant', 20, 'BCA33', 'Male')
# db.add('Ahmad', 20, 'BCA33', 'Male')
# db.add('janmejay', 20, 'BCA33', 'Male')

print(db.search('Prashant'))

data = db.viewall()
print(data)