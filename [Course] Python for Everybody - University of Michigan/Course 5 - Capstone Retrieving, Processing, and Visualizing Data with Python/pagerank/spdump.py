import sqlite3

connection = sqlite3.connect('spider.sqlite')
cursor = connection.cursor()

# Getting page details and links they point to, order by link count
cursor.execute('''SELECT COUNT(from_id) AS links, old_rank, new_rank, id, url 
     FROM Pages JOIN Links ON Pages.id = Links.to_id
     WHERE html IS NOT NULL
     GROUP BY id ORDER BY links DESC''')

print("Inbound Links | Old Rank | New Rank | ID | URL")
count = 0
for row in cursor:
    print(row)
    count = count + 1
print(count, 'complete crawls.')
cursor.close()
