# search_data.py

import sqlite3

conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The dynamic variable we want to search for
search_term = 'Field Medical Kit'

# The SQL command using a '?' placeholder for safety
sql_search = "SELECT part_name, quantity, price FROM Inventory WHERE part_name = ?;"

# Execute the search, passing our variable inside a tuple
cursor.execute(sql_search, (search_term,))
results = cursor.fetchall()

print(f"--- SEARCH RESULTS FOR: {search_term.upper()} ---")
for row in results:
    print(f"Item: {row[0]} | Stock: {row[1]} | Price: ${row[2]}")

if len(results) == 0:
    print("Item not found in the warehouse.")

conn.close()

####

'''
The Base Commander wants to look up the exact stock of a specific item without hard-coding it.
We use a Python variable and a '?' placeholder to safely pass the search term to the database.
'''

'''
CRITICAL SAFETY RULE (Preventing SQL Injection):
Never use standard Python f-strings (e.g., f"SELECT * FROM Inventory WHERE part_name = '{search_term}'") 
to pass variables into SQL. This opens the door to a cyberattack called SQL Injection. 
Always use the '?' placeholder! SQLite will safely sanitize the variable for you.
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

