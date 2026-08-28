# Customer Who Visited but Did Not Make Any Transactions — LeetCode #1581

## Intuition

We need to find customers who visited but did not make any transactions.
A LEFT JOIN keeps every visit, and visits without a matching transaction have a NULL transaction ID.

## Approach

1. LEFT JOIN `Visits` with `Transactions` using `visit_id`.
2. Filter rows where `transaction_id` is NULL.
3. Group the remaining visits by `customer_id`.
4. Count the number of visits without transactions for each customer.

## SQL Concepts

* LEFT JOIN
* ON
* IS NULL
* GROUP BY
* COUNT()
* Table Aliases

## Complexity

Time: O(n)

Space: O(n)

## Key Learning

A LEFT JOIN combined with `IS NULL` can be used to find records that have no matching record in another table.

## Solution

```sql
SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
    ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;
```
