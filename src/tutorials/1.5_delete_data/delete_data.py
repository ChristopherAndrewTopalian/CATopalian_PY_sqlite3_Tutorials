# delete_data.py

import sqlite3

conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command to DELETE existing data
sql_delete = """
DELETE FROM Inventory 
WHERE part_name = 'Night Vision Goggles';
"""

# Execute and save the changes
cursor.execute(sql_delete)
conn.commit() # Always commit when modifying or deleting data!

print("Item successfully deleted from the Military Warehouse database!")

conn.close()

####

'''
A crate of Night Vision Goggles was crushed during a tank training exercise. 
We use the DELETE command to completely remove that row from our active inventory.
'''

'''
CRITICAL SAFETY RULE:
Always include the WHERE clause when deleting! 
If you just write "DELETE FROM Inventory;" without the WHERE clause, 
the database will instantly delete EVERY single row in the table, wiping out your entire warehouse!
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

