# Monthly Transactions I — LeetCode #1193

## Intuition

We need to calculate transaction statistics for each **month and country**.

We can extract the `YYYY-MM` part from `trans_date`, then use conditional aggregation to count approved transactions and calculate their total amount.

## Approach

1. Use `LEFT(trans_date, 7)` to extract the month in `YYYY-MM` format.
2. Group the transactions by `month` and `country`.
3. Use `COUNT(id)` to count all transactions.
4. Use `SUM(state = 'approved')` to count approved transactions.
5. Use `SUM(amount)` to calculate the total transaction amount.
6. Use `SUM((state = 'approved') * amount)` to calculate the total amount of approved transactions.

## Complexity

* Time complexity: **O(n)**
* Space complexity: **O(n)**

## Code

```mysql
SELECT 
    LEFT(trans_date, 7) AS month,
    country, 
    COUNT(id) AS trans_count,
    SUM(state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM((state = 'approved') * amount) AS approved_total_amount
FROM Transactions
GROUP BY month, country;
```

## Key Learning

A condition such as `state = 'approved'` evaluates to `1` when true and `0` when false in MySQL. This allows `SUM()` to be used for **conditional counting and conditional totals**.
