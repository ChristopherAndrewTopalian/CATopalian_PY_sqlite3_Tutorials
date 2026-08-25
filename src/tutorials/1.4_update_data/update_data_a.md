## Updating the Military Warehouse Database

In a logistics depot, inventory never stays still. Troops deploy with gear, and cargo planes drop off new supplies. In this module, we use the SQL `UPDATE` command to change an existing record without having to delete it and start over.

### Line-by-Line Breakdown

**`import sqlite3`**
*   **What it does:** Loads Python's built-in database tools.

**`conn = sqlite3.connect('military_warehouse.db')`**
*   **What it does:** Opens the door to our database file.

**`cursor = conn.cursor()`**
*   **What it does:** Creates our messenger to interact with the database engine.

**`sql_update = """`**
*   **What it does:** Opens a multi-line string to format our SQL command.

**`UPDATE Inventory`**
*   **What it does:** Tells the database engine that we want to modify existing data, and specifically points it to the `Inventory` table.

**`SET quantity = 100`**
*   **What it does:** This is the exact change we want to make. Our previous stock of Kevlar Vests was 150. A platoon just signed out 50 of them, so we are setting the new total quantity to 100.

**`WHERE part_name = 'Kevlar Vest';`**
*   **What it does:** This tells the database exactly *which* row to apply the change to. 
*   **CRITICAL SAFETY WARNING:** The `WHERE` clause is the most important part of an `UPDATE` command. If you forget to include it and simply run `UPDATE Inventory SET quantity = 100`, the database will blindly overwrite the quantity of **every single item** in your entire warehouse to 100, destroying your inventory records! Always double-check your `WHERE` clause.

**`cursor.execute(sql_update)`**
*   **What it does:** Hands the command to the worker to run inside the database.

**`conn.commit()`**
*   **What it does:** Pushes the "Save" button to permanently write this change to the hard drive. 
*   **Why it matters:** Just like when we inserted data, if you do not run `commit()`, the database will discard your updates as soon as the script closes.

**`print("Military Warehouse inventory updated successfully!")`**
*   **What it does:** Gives the user visual confirmation in the terminal.

**`conn.close()`**
*   **What it does:** Safely closes the door to the database file.

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

