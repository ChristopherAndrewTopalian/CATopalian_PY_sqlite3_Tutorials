# read_data.py

import sqlite3

conn = sqlite3.connect('military_warehouse.db')

cursor = conn.cursor()

# The SQL command to SELECT data
sql_select = "SELECT part_name, price FROM Inventory WHERE quantity > 100;"

# Execute and fetch the results
cursor.execute(sql_select)
results = cursor.fetchall()

# Loop through the results (which are returned as Python tuples)
for row in results:
    print(f"Item: {row[0]} | Price: ${row[1]}")

conn.close()

####

'''
Item: Kevlar Vest | Price: $450.5
Item: Field Medical Kit | Price: $75.25
'''

'''
Query (Read) the Data  
The SELECT command grabs the exact data requested from the database.
'''

'''
Explaining the Loop and row[0]
Let's look at the SELECT command we ran:
SELECT part_name, price FROM Inventory WHERE quantity > 100;

Because we asked for exactly two columns in that specific order, and filtered for quantities over 100, SQLite hands us a list of locked tuples that looks like this:
[
    ('Kevlar Vest', 450.50),
    ('Field Medical Kit', 75.25)
]

When we write the for loop, we are just extracting one tuple at a time:

for row in results:
    # On the first loop, row = ('Kevlar Vest', 450.50)
    
    # row[0] is the 1st item: 'Kevlar Vest'
    # row[1] is the 2nd item: 450.50
    
    print(f"Item: {row[0]} | Price: ${row[1]}")
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

