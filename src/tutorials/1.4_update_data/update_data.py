# update_data.py

import sqlite3

conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command to UPDATE existing data
sql_update = """
UPDATE Inventory 
SET quantity = 100 
WHERE part_name = 'Kevlar Vest';
"""

# Execute and save the changes
cursor.execute(sql_update)
conn.commit() # Always commit when modifying data!

print("Military Warehouse inventory updated successfully!")

conn.close()

####

'''
A platoon just signed out 50 Kevlar Vests for deployment. 
We use the UPDATE command to change the existing quantity from 150 down to 100.
'''

'''
CRITICAL SAFETY RULE:
Always include the WHERE clause when updating! 
If you just write "UPDATE Inventory SET quantity = 100;" without the WHERE clause, 
the database will change the quantity of EVERY single item in the entire warehouse to 100!
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

