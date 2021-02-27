import sqlite3

connection = sqlite3.connect('spider.sqlite')
cursor = connection.cursor()

# Getting every from_id once in Links table
cursor.execute('''SELECT DISTINCT from_id FROM Links''')
from_ids = list()
for row in cursor:
    from_ids.append(row[0])

# Getting every from_id pointing to_id once in Links table
cursor.execute('''SELECT DISTINCT from_id, to_id FROM Links''')
to_ids = list()
links = list()
for row in cursor:
    from_id = row[0]
    to_id = row[1]

    # Not counting pages point to themselves
    if from_id == to_id:
        continue

    if from_id not in from_ids:
        continue
    if to_id not in from_ids:
        continue

    links.append(row)

    if to_id not in to_ids:
        to_ids.append(to_id)

# Saving actual ranks to old_ranks
old_ranks = dict()
for node in from_ids:
    cursor.execute('''SELECT new_rank FROM Pages WHERE id = ?''', (node,))
    row = cursor.fetchone()
    old_ranks[node] = row[0]

iterations = input('How many iterations:')
count = 1
if len(iterations) > 0:
    count = int(iterations)

# If there is no record to rank, quit
if len(old_ranks) < 1:
    print("There is no data to rank.")
    quit()

# Page ranking loop
for i in range(count):
    new_ranks = dict()
    total = 0.0
    for (node, old_rank) in list(old_ranks.items()):
        total = total + old_rank
        new_ranks[node] = 0.0

    # Find the number of outbound links and sent the page rank down each
    for (node, old_rank) in list(old_ranks.items()):
        give_ids = list()
        for (from_id, to_id) in links:
            if from_id != node:
                continue
            if to_id not in to_ids:
                continue
            give_ids.append(to_id)
        if len(give_ids) < 1:
            continue
        amount = old_rank / len(give_ids)

        for item in give_ids:
            new_ranks[item] = new_ranks[item] + amount

    new_total = 0
    for (node, next_rank) in list(new_ranks.items()):
        new_total = new_total + next_rank
    evap = (total - new_total) / len(new_ranks)

    for node in new_ranks:
        new_ranks[node] = new_ranks[node] + evap

    new_total = 0
    for (node, next_rank) in list(new_ranks.items()):
        new_total = new_total + next_rank

    # Computing the per-page average change from old rank to new rank
    total_diff = 0
    for (node, old_rank) in list(old_ranks.items()):
        new_rank = new_ranks[node]
        diff = abs(old_rank-new_rank)
        total_diff = total_diff + diff

    avg_diff = total_diff / len(old_ranks)
    print("Iteration", i + 1, "Average Differece ->", avg_diff)

    old_ranks = new_ranks

# Printing id of the page and its new rank
print(list(new_ranks.items()))

# Setting pages actual rank to old_rank in Pages table
cursor.execute('''UPDATE Pages SET old_rank=new_rank''')

# Setting new computed ranks to new_rank in Pages table
for(item, new_rank) in list(new_ranks.items()):
    cursor.execute('''UPDATE Pages SET new_rank=? WHERE id=?''', (new_rank, item))

connection.commit()
cursor.close()
