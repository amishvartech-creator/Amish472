# SQL FOR DATA ANALYTICS.MD


**Theme: Retail Sales Exploration**

1. What is the functional difference between SELECT * and specifying column
   names, and when is each preferred?

   **Answer**

   ````

   ## Functional difference

- `SELECT *` returns all columns from the table(s) in the result set.
- `SELECT col1, col2, ...` returns only the named columns.


## When each is preferred

- Use `SELECT *`:
  - For quick ad-hoc queries or exploring data.
  - When you need every column and the table schema is stable.
- Use explicit columns:
  - In production queries, reports, APIs, or joins.
  - When you want predictable output, better performance, and less data transfer.
  - When the table schema may change, or you want to avoid returning unnecessary or sensitive columns.

## Why explicit columns are usually better

- More efficient: only fetches the needed data.
- Safer: avoids broken code if columns are added/removed or order changes.
- Clearer: makes the query intent easier to understand.
- Better for joins: avoids ambiguous or duplicate column names.

> In short: `SELECT *` is fine for quick checks, but listing columns is best for maintainable, efficient SQL.


````


2. Which keyword renames a column in the output, and does this alias change
   the actual table structure in the database?

   **Answer**


  ````


  - The keyword is `AS` (e.g. `SELECT sales_amount AS total_sales`).
  - You can also alias without `AS` in many SQL dialects: `SELECT sales_amount total_sales`.

## Does it change the table structure?

- No.
- An alias only changes the column name in that query result.
- It does not modify the underlying table or database schema.


````



3. Why does wrapping a numeric value in quotes (e.g., '5000') in a WHERE clause
   create a data type conflict in SQL?

   **Answer**

    ````

   ## Why quoted numbers cause data type conflicts

   - `'5000'` is a string literal, not a numeric literal.
   - In a `WHERE` clause, comparing a string to a numeric column forces SQL to convert types.
   - If the column is numeric, the database may attempt implicit conversion and fail if the string is not a valid number or if the engine does not allow the comparison.
    - This can produce an error or unexpected behavior because the types differ.

   ### Best practice

- Use unquoted numeric values for numeric columns:
  - `WHERE price = 5000`
- Use quotes only for text values:
  - `WHERE product_name = '5000'`



  ````


4. Contrast the results of ORDER BY Profit DESC versus ASC when the goal is to
     identify the top 10 most profitable orders.

     **Answer**


     ````

     ## Contrast: `ORDER BY Profit DESC` vs `ASC`

    `ORDER BY Profit DESC`
   - Sorts values from highest to lowest.
   - Best for finding top 10 most profitable orders.
   - Example: highest profit first.

   - `ORDER BY Profit ASC`
   - Sorts values from lowest to highest.
   - Returns the least profitable orders first.
   - Not appropriate when you want the top profitable orders.

     ### In short
     - Use `DESC` to identify the top 10 most profitable orders.
     - `ASC` would give the bottom 10 instead.

     ````


5. What is the T-SQL equivalent of the LIMIT clause in MS SQL Server, and why
   does syntax vary across SQL engines?

   **Answer**

   ````

   ## Answer

- In T-SQL (MS SQL Server), the equivalent of `LIMIT` is usually:
  - `SELECT TOP N ...`
  - Example: `SELECT TOP 10 * FROM Orders ORDER BY Profit DESC`

- Newer SQL Server versions also support:
  - `ORDER BY ... OFFSET ... FETCH NEXT ... ROWS ONLY`
  - Example:
    - `SELECT * FROM Orders ORDER BY Profit DESC OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY`

## Why syntax varies across SQL engines

- Different databases implemented different SQL feature sets and extensions.
- Some use older proprietary syntax (`TOP` in SQL Server, `LIMIT` in MySQL/PostgreSQL, `ROWNUM` in Oracle older versions).
- Standards evolved over time, so engines support different dialects and compatibility behaviors.
- As a result, the same idea is expressed with different syntax in different SQL systems.

````


6. Explain the logical execution order of a query containing SELECT, WHERE, ORDER
   BY, and LIMIT clauses.

   **Answer*

   ````

   ## Logical execution order

1. `WHERE`
   - Filters rows from the source data first.
   - Only rows that satisfy the condition move on.

2. `SELECT`
   - Chooses which columns or expressions appear in the result.
   - Happens after filtering, so it works on the narrowed row set.

3. `ORDER BY`
   - Sorts the selected rows next.
   - Determines the final order of the result set.

4. `LIMIT`
   - Applies last to keep only the top N rows from the sorted result.
   - If you want the top values, `LIMIT` must come after `ORDER BY`.

> In SQL logic, `WHERE` filters, `SELECT` projects, `ORDER BY` sorts, and `LIMIT` truncates.

````






