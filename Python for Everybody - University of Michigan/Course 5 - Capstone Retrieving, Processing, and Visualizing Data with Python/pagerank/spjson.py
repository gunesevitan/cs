import sqlite3

connection = sqlite3.connect('spider.sqlite')
cursor = connection.cursor()

print("Writing JSON output on spider.js")
# Displaying number of pages from highest to lowest rank
node_count = int(input("How many nodes? "))

# Getting page details and links they point to, order by id and link count
cursor.execute('''SELECT COUNT(from_id) AS links, old_rank, new_rank, id, url 
    FROM Pages JOIN Links ON Pages.id = Links.to_id
    WHERE html IS NOT NULL AND ERROR IS NULL
    GROUP BY id ORDER BY id,links''')


handle = open('spider.js', 'w')
nodes = list()
max_rank = None
min_rank = None

for row in cursor:
    nodes.append(row)
    rank = row[2]
    if max_rank is None or max_rank < rank:
        max_rank = rank
    if min_rank is None or min_rank > rank:
        min_rank = rank
    if len(nodes) > node_count:
        break

if max_rank == min_rank or max_rank is None or min_rank is None:
    print("Error - Run ranker.py to compute page rank first.")
    quit()


handle.write('spiderJson = {"nodes":[\n')
count = 0
node_map = dict()
ranks = dict()
for row in nodes:
    if count > 0:
        handle.write(',\n')
    rank = row[2]
    rank = 19 * ((rank - min_rank) / (max_rank - min_rank))
    handle.write('{' + '"weight":' + str(row[0]) + ',"rank":' + str(rank) + ',')
    handle.write(' "id":' + str(row[3]) + ', "url":"' + row[4] + '"}')
    node_map[row[3]] = count
    ranks[row[3]] = rank
    count = count + 1
handle.write('],\n')

cursor.execute('''SELECT DISTINCT from_id, to_id FROM Links''')
handle.write('"links":[\n')

count = 0
for row in cursor:
    if row[0] not in node_map or row[1] not in node_map:
        continue
    if count > 0:
        handle.write(',\n')
    rank = ranks[row[0]]
    srank = 19 * ((rank - min_rank) / (max_rank - min_rank))
    handle.write('{"source":' + str(node_map[row[0]]) + ',"target":' + str(node_map[row[1]]) + ',"value":3}')
    count = count + 1
handle.write(']};')
handle.close()
cursor.close()

print("Open force.html in a browser to view the visualization.")
