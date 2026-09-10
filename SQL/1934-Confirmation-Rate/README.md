# Confirmation Rate — LeetCode #1934

## Intuition

We need to calculate the **confirmation rate for each user**.

A confirmation has an action of `"confirmed"`, so we can treat it as `1`. Any other action is treated as `0`. The average of these values gives the confirmation rate.

We use a `LEFT JOIN` so that users with no confirmation records are also included.

## Approach

1. Start with the `Signups` table because we need every user.
2. Use `LEFT JOIN` to connect each user with their confirmation records.
3. Use `IF()`:

   * `"confirmed"` → `1`
   * otherwise → `0`
4. Use `AVG()` to calculate the average confirmation value.
5. Use `ROUND(..., 2)` to round the result to 2 decimal places.
6. Use `GROUP BY` to calculate the rate separately for each user.

## Complexity

* Time complexity: **O(n)**
* Space complexity: **O(n)**

## Code

```mysql
# Write your MySQL query statement below

SELECT
    s.user_id,
    ROUND(
        AVG(IF(c.action = "confirmed", 1, 0)),
        2
    ) AS confirmation_rate
FROM Signups AS s
LEFT JOIN Confirmations AS c
    ON s.user_id = c.user_id
GROUP BY s.user_id;
```

## Key Learning

`LEFT JOIN` is useful when we need to keep all rows from the first table, even when there is no matching row in the second table.

`IF()` can convert a condition into `1` or `0`, and `AVG()` can then be used to calculate a rate.
