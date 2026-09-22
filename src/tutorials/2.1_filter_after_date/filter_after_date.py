# filter_after_date.py

import sqlite3

conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The dynamic date we want to filter by
target_date = '2026-01-01'

# SQL command to find everything delivered AFTER the target date
sql_filter = "SELECT part_name, quantity, delivery_date FROM Inventory WHERE delivery_date > ?;"

cursor.execute(sql_filter, (target_date,))
results = cursor.fetchall()

print(f"SHIPMENTS RECEIVED AFTER {target_date}")
for row in results:
    print(f"Item: {row[0]} | Stock: {row[1]} | Delivered: {row[2]}")

conn.close()

'''
SHIPMENTS RECEIVED AFTER 2026-01-01
Item: Night Vision Goggles | Stock: 45 | Delivered: 2026-02-10
Item: Field Medical Kit | Stock: 300 | Delivered: 2026-08-24
Item: Combat Boots | Stock: 220 | Delivered: 2026-01-05
Item: MRE Case | Stock: 500 | Delivered: 2026-03-22
Item: Ammunition Crate | Stock: 80 | Delivered: 2026-01-30
Item: First Aid Pouch | Stock: 175 | Delivered: 2026-02-14
Item: Camouflage Netting | Stock: 95 | Delivered: 2026-04-02
'''