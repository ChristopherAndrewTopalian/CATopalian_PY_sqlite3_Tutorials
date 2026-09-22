# update_data.py

import sqlite3

conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command using the '?' Security Shield
sql_update = """
UPDATE Inventory 
SET quantity = ? 
WHERE part_name = ?
"""

# The data values neatly organized in a tuple
# Order matters: The first item (100) maps to the first ?, 
# the second item ('Kevlar Vest') maps to the second ?.
update_values = (100, 'Kevlar Vest')

# Execute and safely merge the command with the data
cursor.execute(sql_update, update_values)

conn.commit() # Always commit when modifying data

print("Military Warehouse inventory updated successfully!")

conn.close()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

