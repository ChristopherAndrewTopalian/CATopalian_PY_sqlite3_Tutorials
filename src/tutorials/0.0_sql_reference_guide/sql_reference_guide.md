# SQL Quick Reference - Node.js (node:sqlite)

A cheat-sheet companion to the Military Warehouse tutorial series. Every example uses the same
`Inventory` table (`id`, `part_name`, `quantity`, `delivery_date`) so the syntax stays familiar.
Two connection methods appear throughout:

- **`db.exec(sql)`** - runs SQL that doesn't return rows (CREATE, DROP, INSERT, UPDATE, DELETE).
- **`db.prepare(sql)`** - builds a statement you then call `.run()`, `.get()`, or `.all()` on
  (used for anything that returns rows, or that takes `?` parameters).

---

## Table & Schema Commands (DDL)

| SQL Keyword | What It Does | Node.js Example | When You'd Use It |
|---|---|---|---|
| `CREATE TABLE` | Defines a new table and its columns | `db.exec("CREATE TABLE Inventory (id INTEGER PRIMARY KEY, part_name TEXT, quantity INTEGER, delivery_date TEXT);")` | Setting up your database structure for the first time |
| `CREATE TABLE IF NOT EXISTS` | Same as above, but skips silently if the table already exists | `db.exec("CREATE TABLE IF NOT EXISTS Inventory (...);")` | Scripts that might be run more than once, without erroring |
| `DROP TABLE` | Permanently deletes a table and all its data | `db.exec("DROP TABLE Inventory;")` | Wiping a table clean before rebuilding it (careful - irreversible) |
| `DROP TABLE IF EXISTS` | Same as above, but won't error if the table doesn't exist | `db.exec("DROP TABLE IF EXISTS Inventory;")` | Safe "reset" step at the top of a seed script |
| `ALTER TABLE ... ADD COLUMN` | Adds a new column to an existing table | `db.exec("ALTER TABLE Inventory ADD COLUMN supplier TEXT;")` | Your schema needs to grow after data already exists |
| `CREATE INDEX` | Builds a lookup structure on a column, speeding up searches/filters on it | `db.exec("CREATE INDEX idx_delivery_date ON Inventory(delivery_date);")` | Any column you filter or sort by often, especially at scale |
| `CREATE INDEX IF NOT EXISTS` | Same as above, safe to re-run | `db.exec("CREATE INDEX IF NOT EXISTS idx_delivery_date ON Inventory(delivery_date);")` | Setup scripts that may run more than once |
| `DROP INDEX` | Removes an index | `db.exec("DROP INDEX idx_delivery_date;")` | Rare - usually only when redesigning your query patterns |

---

## Reading Data (SELECT)

| SQL Keyword | What It Does | Node.js Example | When You'd Use It |
|---|---|---|---|
| `SELECT *` | Returns every column | `db.prepare("SELECT * FROM Inventory;").all()` | Quick look at everything - avoid in production, it's wasteful |
| `SELECT col1, col2` | Returns only the columns you name | `db.prepare("SELECT part_name, price FROM Inventory;").all()` | You know exactly what you need - faster and clearer |
| `WHERE` | Filters rows by a condition | `db.prepare("SELECT * FROM Inventory WHERE quantity > ?;").all(100)` | Only want rows matching some rule |
| `ORDER BY ... ASC` | Sorts results smallest/earliest first | `db.prepare("SELECT * FROM Inventory ORDER BY quantity ASC;").all()` | "Lowest stock first" type reports |
| `ORDER BY ... DESC` | Sorts results largest/latest first | `db.prepare("SELECT * FROM Inventory ORDER BY delivery_date DESC;").all()` | "Most recent first" type reports |
| `LIMIT` | Caps how many rows come back | `db.prepare("SELECT * FROM Inventory LIMIT 5;").all()` | Top-5 lists, pagination, sampling a big table |
| `DISTINCT` | Removes duplicate rows from the result | `db.prepare("SELECT DISTINCT part_name FROM Inventory;").all()` | "What are all the unique X values?" |
| `COUNT(*)` | Counts matching rows | `db.prepare("SELECT COUNT(*) AS total FROM Inventory;").get()` | "How many items do we have?" |
| `SUM(col)` | Adds up a numeric column | `db.prepare("SELECT SUM(quantity) AS total_units FROM Inventory;").get()` | Total stock, total revenue, etc. |
| `AVG(col)` | Averages a numeric column | `db.prepare("SELECT AVG(price) AS avg_price FROM Inventory;").get()` | "What's the typical price?" |
| `MIN(col)` / `MAX(col)` | Smallest / largest value in a column | `db.prepare("SELECT MIN(quantity) AS lowest FROM Inventory;").get()` | Cheapest item, oldest date, lowest stock, etc. |
| `GROUP BY` | Buckets rows together for aggregate functions | `db.prepare("SELECT part_name, SUM(quantity) FROM Inventory GROUP BY part_name;").all()` | "Totals per category" type reports |
| `HAVING` | Filters *after* grouping (WHERE can't do this) | `db.prepare("SELECT part_name, COUNT(*) c FROM Inventory GROUP BY part_name HAVING c > 1;").all()` | Filtering on an aggregate result, like "groups with more than 1 entry" |
| `LIKE` | Fuzzy text matching with wildcards (`%` = anything) | `db.prepare("SELECT * FROM Inventory WHERE part_name LIKE ?;").all('%Vest%')` | Search boxes, partial-name lookups |
| `IN (...)` | Matches any value in a list | `db.prepare("SELECT * FROM Inventory WHERE part_name IN (?, ?);").all('Kevlar Vest', 'MRE Case')` | "Any of these specific items" |
| `BETWEEN` | Matches a range (inclusive) | `db.prepare("SELECT * FROM Inventory WHERE quantity BETWEEN ? AND ?;").all(50, 200)` | Range filters - dates, prices, quantities |
| `IS NULL` / `IS NOT NULL` | Checks for missing data | `db.prepare("SELECT * FROM Inventory WHERE supplier IS NULL;").all()` | Finding incomplete records |
| `JOIN` (`INNER JOIN`) | Combines rows from two tables where a condition matches | `db.prepare("SELECT * FROM Inventory JOIN Suppliers ON Inventory.supplier_id = Suppliers.id;").all()` | Data split across related tables |
| `LEFT JOIN` | Like JOIN, but keeps unmatched rows from the first table too | `db.prepare("SELECT * FROM Inventory LEFT JOIN Suppliers ON Inventory.supplier_id = Suppliers.id;").all()` | "Show everything, even if some don't have a match" |
| `AS` | Renames a column or table in the result | `db.prepare("SELECT part_name AS item FROM Inventory;").all()` | Cleaner output labels, especially with aggregates |

---

## Changing Data (INSERT / UPDATE / DELETE)

| SQL Keyword | What It Does | Node.js Example | When You'd Use It |
|---|---|---|---|
| `INSERT INTO` | Adds new row(s) | `db.exec("INSERT INTO Inventory (part_name, quantity) VALUES ('Kevlar Vest', 150);")` | Adding new records |
| `INSERT INTO` (parameterized) | Same, but with a dynamic/safe value | `db.prepare("INSERT INTO Inventory (part_name, quantity) VALUES (?, ?);").run('Kevlar Vest', 150)` | Any time the value comes from a variable, not hardcoded text |
| `UPDATE ... SET` | Modifies existing row(s) | `db.exec("UPDATE Inventory SET quantity = 100 WHERE part_name = 'Kevlar Vest';")` | Correcting or changing existing data |
| `DELETE FROM` | Removes row(s) | `db.exec("DELETE FROM Inventory WHERE part_name = 'Night Vision Goggles';")` | Removing records you no longer need |

---

## Node.js `node:sqlite` Execution Methods

| Method | What It Does | When You'd Use It |
|---|---|---|
| `db.exec(sql)` | Runs SQL with no return value and no parameters | CREATE, DROP, ALTER, or simple hardcoded INSERT/UPDATE/DELETE |
| `db.prepare(sql)` | Builds a reusable statement object | Any query with `?` parameters, or any SELECT |
| `stmt.run(...args)` | Executes a prepared statement, returns metadata (rows changed, last insert ID) - no result rows | Parameterized INSERT, UPDATE, DELETE |
| `stmt.get(...args)` | Executes and returns **one** row as an object | You expect exactly one result (a single match, a `COUNT(*)`, etc.) |
| `stmt.all(...args)` | Executes and returns **every** matching row as an array of objects | Any query where you expect multiple rows |
| `db.close()` | Closes the database connection | Always call this when your script is done |

---

## Quick Notes

- **No `.commit()` needed** - `node:sqlite` auto-commits every statement immediately, unlike Python's `sqlite3`.
- **Always use `?` placeholders for dynamic values** - never build SQL strings with template literals or concatenation when the value comes from user input or a variable. That's what prevents SQL injection.
- **Rows come back as plain JS objects** - `row.part_name`, not `row[0]`.

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

