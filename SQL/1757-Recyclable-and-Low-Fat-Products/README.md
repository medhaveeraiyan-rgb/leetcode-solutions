# Recyclable and Low Fat Products — LeetCode #1757

## Intuition

We need to find products that are both low fat and recyclable.
So, we filter the Products table using two conditions.

## Approach

1. Select `product_id`.
2. Use `WHERE` to filter the products.
3. Use `AND` because both conditions must be true.

## SQL Concepts

- SELECT
- FROM
- WHERE
- AND
- Comparison operator `=`

## Complexity

Time: O(n)

Space: O(n) for the output.

## Key Learning

`AND` is used when all specified conditions must be true.

## Solution

```sql
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
