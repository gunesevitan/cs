import sqlite3

connection = sqlite3.connect('spider.sqlite')
cursor = connection.cursor()

# Setting all pages new_rank to 1.0 and old_rank to 0.0
cursor.execute('''UPDATE Pages SET new_rank=1.0, old_rank=0.0''')
connection.commit()

cursor.close()

print("All pages set to a rank of 1.0")
