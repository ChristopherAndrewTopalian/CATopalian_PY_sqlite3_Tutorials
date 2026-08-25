## Deleting from the Military Warehouse Database

Sometimes inventory isn't just modified; it is permanently destroyed or decommissioned. If a crate of equipment is damaged beyond repair during a training exercise, it must be officially written off. In this module, we use the SQL `DELETE` command to permanently remove a specific row from our database.

### Line-by-Line Breakdown

**`import sqlite3`**
*   **What it does:** Loads Python's built-in database tools.

**`conn = sqlite3.connect('military_warehouse.db')`**
*   **What it does:** Opens the door to our database file.

**`cursor = conn.cursor()`**
*   **What it does:** Creates our messenger to interact with the database engine.

**`sql_delete = """`**
*   **What it does:** Opens a multi-line string to format our SQL command cleanly.

**`DELETE FROM Inventory`**
*   **What it does:** Tells the database engine that we want to remove data, and points it to the `Inventory` table.

**`WHERE part_name = 'Night Vision Goggles';`**
*   **What it does:** This tells the database exactly *which* row to target and destroy. 
*   **CRITICAL SAFETY WARNING:** Just like the `UPDATE` command, the `WHERE` clause is the absolute most important part of a `DELETE` command. If you forget to include it and simply run `DELETE FROM Inventory;`, the database will instantly delete **every single row** in your table. It will wipe out your entire warehouse in a millisecond. Always double-check your `WHERE` clause before running a delete command!

**`cursor.execute(sql_delete)`**
*   **What it does:** Hands the command to the worker to run inside the database.

**`conn.commit()`**
*   **What it does:** Pushes the "Save" button to permanently authorize this deletion on the hard drive. 
*   **Why it matters:** If you do not run `commit()`, the database will cancel the deletion process as soon as the script closes, and the data will remain exactly as it was.

**`print("Item successfully deleted from the Military Warehouse database!")`**
*   **What it does:** Gives the user visual confirmation in the terminal that the row was removed.

**`conn.close()`**
*   **What it does:** Safely closes the door to the database file.

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

