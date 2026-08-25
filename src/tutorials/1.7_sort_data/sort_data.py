# sort_data.py

import sqlite3

conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command to SELECT data and sort it
sql_sort = "SELECT part_name, quantity, price FROM Inventory ORDER BY quantity ASC;"

# Execute and fetch the results
cursor.execute(sql_sort)
results = cursor.fetchall()

print("CRITICAL REORDER LIST (LOWEST STOCK FIRST)")
for row in results:
    print(f"Item: {row[0]} | Stock: {row[1]} | Unit Cost: ${row[2]}")

conn.close()

####

'''
The Quartermaster needs to know which items are closest to running out.
We use the ORDER BY command to automatically sort the results before Python even receives them.
'''

'''
ASC vs DESC:
ASC (Ascending) sorts from smallest to largest (A-Z, 1-100). This is the default if you leave it blank.
DESC (Descending) sorts from largest to smallest (Z-A, 100-1). Perfect for finding the most expensive items!
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

