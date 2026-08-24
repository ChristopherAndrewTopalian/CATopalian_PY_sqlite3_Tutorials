# insert_data.py

import sqlite3

conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command to INSERT data
sql_insert = """
INSERT INTO Inventory (part_name, quantity, price) 
VALUES 
    ('Night Vision Goggles', 45, 2500.00),
    ('Kevlar Vest', 150, 450.50),
    ('Field Medical Kit', 300, 75.25);
"""

cursor.execute(sql_insert)
conn.commit() # Always commit when making changes!
conn.close()

print("Military Warehouse data inserted successfully!")

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

