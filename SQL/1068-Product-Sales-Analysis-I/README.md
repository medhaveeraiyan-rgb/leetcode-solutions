# Product Sales Analysis I — LeetCode #1068

## Intuition

We need the product name along with the year and price of each sale.
The Sales and Product tables are connected using product_id, so we JOIN them using that column.

## Approach

1. Select product_name from the Product table.
2. Select year and price from the Sales table.
3. JOIN the two tables using their common product_id.
4. Return the matching product and sales information.

## SQL Concepts

- SELECT
- FROM
- JOIN
- ON
- Table Aliases
- Primary Key
- Foreign Key

## Complexity

Time: O(n)

Space: O(n)

## Key Learning

A JOIN connects related tables using a common key.

## Solution

```sql
SELECT p.product_name, s.year, s.price
FROM Sales s
JOIN Product p
    ON p.product_id = s.product_id;
