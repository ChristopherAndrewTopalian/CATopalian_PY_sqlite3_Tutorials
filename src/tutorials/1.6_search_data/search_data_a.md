## Dynamic Searching in the Military Warehouse

Up until now, we have hard-coded our search terms directly into the SQL string. But in the real world, a Quartermaster or Base Commander will want to type a word into a search bar and get the results instantly. In this module, we learn how to safely pass a Python variable into an SQLite query.

### Line-by-Line Breakdown

**`import sqlite3`**
*   **What it does:** Loads Python's built-in database tools.

**`conn = sqlite3.connect('military_warehouse.db')`**
*   **What it does:** Opens the door to our database file.

**`cursor = conn.cursor()`**
*   **What it does:** Creates our messenger to interact with the database engine.

**`search_term = 'Field Medical Kit'`**
*   **What it does:** Creates a standard Python variable. In a real application, this variable would come from a user typing into a search box on a website or terminal.

**`sql_search = "SELECT part_name, quantity, price FROM Inventory WHERE part_name = ?;"`**
*   **What it does:** This is our SQL query, but with a major difference: the `?` symbol. 
*   **The Placeholder (`?`):** Instead of typing the item name directly, we use `?` as a blank placeholder. It tells the SQLite engine, "I am going to give you a variable to put here in a moment."

**`cursor.execute(sql_search, (search_term,))`**
*   **What it does:** Hands the command to the worker, but also hands it the variable to fill in the blank.
*   **Why the comma? `(search_term,)`**: SQLite requires the variables to be passed as a locked tuple. In Python, if you only have one item in a tuple, you *must* put a comma after it, or Python gets confused and thinks it is just a regular math parenthesis.
*   **CRITICAL SECURITY WARNING:** You might wonder why we do not just use a Python f-string (like `f"WHERE part_name = '{search_term}'"`). **Never do this.** Using f-strings to pass variables into SQL opens your database to a cyberattack called "SQL Injection," where a hacker can type malicious code into your search bar and destroy your database. The `?` placeholder automatically sanitizes the input and protects your military data!

**`results = cursor.fetchall()`**
*   **What it does:** Grabs all the matching rows.

**`for row in results:`**
*   **What it does:** Loops through the found data and prints the item name, stock, and price to the screen.

**`if len(results) == 0:`**
*   **What it does:** A helpful Python check. If the database returns 0 rows, it tells the Commander the item does not exist in the warehouse.

**`conn.close()`**
*   **What it does:** Safely closes the door to the database.

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

