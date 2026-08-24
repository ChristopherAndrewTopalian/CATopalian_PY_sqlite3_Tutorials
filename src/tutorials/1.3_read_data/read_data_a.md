## Querying the Military Warehouse Database

With our depot stocked, we need a way to audit our supplies. In this module, we use the SQL `SELECT` command to search our database and retrieve specific information instantly, filtering out what we don't need.

### Line-by-Line Breakdown

**`import sqlite3`**
*   **What it does:** Loads Python's built-in database tools.

**`conn = sqlite3.connect('military_warehouse.db')`**
*   **What it does:** Opens the door to our military database file.

**`cursor = conn.cursor()`**
*   **What it does:** Creates our messenger to interact with the database engine.

**`sql_select = "SELECT part_name, price FROM Inventory WHERE quantity > 100;"`**
*   **What it does:** This is the core SQL query. 
*   **`SELECT part_name, price`**: Tells the database exactly which columns we want to see. We don't need the `id` or the `quantity` returned, just the name and the cost.
*   **`FROM Inventory`**: Specifies which table to search.
*   **`WHERE quantity > 100`**: This is our filter. Instead of loading the entire warehouse into memory, the database only returns items that have more than 100 units in stock.

**`cursor.execute(sql_select)`**
*   **What it does:** Hands the query to the worker to run inside the database engine.

**`results = cursor.fetchall()`**
*   **What it does:** Grabs all the matching rows that the database found and saves them into a Python variable named `results`. 

**`for row in results:`**
*   **What it does:** Starts a Python loop that looks at one row of data at a time.

**`print(f"Item: {row[0]} | Price: ${row[1]}")`**
*   **What it does:** Uses an f-string to cleanly print the data to the screen.

### Explaining the Loop and `row[0]`

When `fetchall()` grabs the data, SQLite intentionally returns it as a list of locked Python "tuples" (lists that use parentheses and cannot be accidentally modified). 

Because we specifically asked for `part_name` and `price` in our `SELECT` statement, the database hands us a list that looks like this:
```python
[
    ('Kevlar Vest', 450.50),
    ('Field Medical Kit', 75.25)
]
```

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

