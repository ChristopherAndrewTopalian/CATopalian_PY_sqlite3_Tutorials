# database_connect_or_create.py

import sqlite3

# Connect to the database (it creates the file automatically if it doesn't exist)
conn = sqlite3.connect('military_warehouse.db')

# Think of the cursor as the worker inside the database.
# The cursor is the tool you actually use to run SQL commands and navigate through the rows returned.
# This creates a cursor object attached to that open connection made above.
cursor = conn.cursor()

# SQL command to CREATE a table named Inventory
# Inventory table has id, part_name, quantity and price
sql_command = """
CREATE TABLE IF NOT EXISTS Inventory (
    id INTEGER PRIMARY KEY,
    part_name TEXT,
    quantity INTEGER,
    price REAL
);
"""
# REAL is a data type for a floating point number, aka decimal numbers.

# Execute and save
cursor.execute(sql_command)
conn.commit()
conn.close()

print("Military Warehouse Database and Table created successfully!")

####

'''
This script creates a local file called military_warehouse.db and sets up a table (like a spreadsheet) with strict columns.
'''

'''
What Does the Cursor Actually Do?
The cursor handles two primary jobs:

1. Executing SQL Commands (.execute())
You tell the cursor what SQL statement to run:
cursor.execute("SELECT part_name, price FROM Inventory WHERE price > 50")

2. Fetching and Tracking Rows (.fetchone(), .fetchall())
When the database finds matching rows, the cursor acts like a bookmark pointing at the current row:

cursor.fetchone() - Grabs the next single row and moves the pointer forward by one.

cursor.fetchall() - Grabs all remaining matching rows at once as a list.

cursor.fetchmany(10) - Grabs the next 10 rows (ideal for streaming chunks of data without overloading memory).
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

