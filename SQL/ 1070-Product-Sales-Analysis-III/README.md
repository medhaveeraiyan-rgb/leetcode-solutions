# Product Sales Analysis III — LeetCode #1070

## Intuition

We need to find the **first year each product was sold** and return the quantity and price of the sale in that first year.

First, find the minimum year for every product. Then select the rows whose `(product_id, year)` matches those first years.

## Approach

1. Use `MIN(year)` to find the first year for each product.
2. Use `GROUP BY product_id` to calculate the first year separately for every product.
3. Use a subquery to get `(product_id, first_year)` for every product.
4. Use `(product_id, year) IN (...)` to keep only the sales records from the first year.
5. Select `product_id`, the first year, `quantity`, and `price`.

## Complexity

* Time complexity: **O(n)**
* Space complexity: **O(n)**

## Code

```mysql
# Write your MySQL query statement below

SELECT 
    product_id, 
    year AS first_year, 
    quantity, 
    price
FROM Sales
WHERE (product_id, year) IN (
    SELECT 
        product_id, 
        MIN(year)
    FROM Sales
    GROUP BY product_id
);
```

## Key Learning

The pattern

```sql
WHERE (column1, column2) IN (
    SELECT column1, MIN(column2)
    FROM table
    GROUP BY column1
)
```

is useful when we need to find the **earliest/latest record for each group**.
