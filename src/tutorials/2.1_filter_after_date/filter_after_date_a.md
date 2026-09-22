## Filtering Data: After a Specific Date

Welcome to Chapter 2: Advanced Filtering. In a military warehouse, tracking exactly *when* assets arrive is a matter of national security. The Quartermaster needs to know what shipments arrived after a certain date to verify supply chain efficiency. In this module, we use the `WHERE` clause combined with the greater-than (`>`) operator to filter records by date.

### The SQLite Date Secret
SQLite is designed to be lightweight, which means it actually does not have a dedicated `DATE` data type! Instead, database engineers store dates as standard `TEXT` columns using the strict ISO8601 format: **`YYYY-MM-DD`**. 

Because numbers and text are sorted alphabetically by computers, asking the database if `'2026-08-24'` is greater than `'2026-01-01'` works perfectly.

### Line-by-Line Breakdown

*(Note: The script includes a small setup block to add the `delivery_date` column to our database so we have dates to filter!)*

**`target_date = '2026-01-01'`**
*   **What it does:** Sets up our dynamic Python variable formatted as a strict `YYYY-MM-DD` string.

**`sql_filter = "SELECT part_name, quantity, delivery_date FROM Inventory WHERE delivery_date > ?;"`**
*   **What it does:** This is the core filtering query. 
*   **`WHERE delivery_date > ?`**: We instruct the SQLite engine to look at the text in the date column. If the year, month, and day are numerically "higher" (meaning later in time) than our placeholder, the database will return that row. 
*   **The Placeholder (`?`)**: Once again, we use the question mark to safely pass our variable into the SQL engine, completely protecting the warehouse from SQL Injection attacks.

**`cursor.execute(sql_filter, (target_date,))`**
*   **What it does:** Hands the command to the worker, locking our `target_date` safely inside a tuple `(target_date,)` so SQLite can replace the `?` placeholder.

**`results = cursor.fetchall()`**
*   **What it does:** Grabs all the rows that passed our date filter. The database leaves the older 2025 shipments behind and only hands Python the fresh 2026 deliveries.

**`for row in results:`**
*   **What it does:** Loops through the filtered data and prints the item name, stock, and delivery date clearly to the terminal screen.

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

