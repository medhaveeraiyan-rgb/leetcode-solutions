# User Activity for the Past 30 Days I — LeetCode #1141

## Intuition

We need to find the number of **unique active users for each day** during the 30-day period ending on `2019-07-27`.

For each date, count the distinct users who performed at least one activity.

## Approach

1. Use `DATE_SUB()` to calculate the date 29 days before `2019-07-27`.
2. Use `BETWEEN` to select activities from the 30-day period, including both the start and end dates.
3. Use `COUNT(DISTINCT user_id)` to count unique active users on each day.
4. Group the result by `activity_date` so that we get one row for each day.

## Complexity

* Time complexity: **O(n)**
* Space complexity: **O(n)**

## Code

```mysql id="k3v8pa"
# Write your MySQL query statement below

SELECT 
    activity_date AS day, 
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date 
    BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) 
    AND '2019-07-27'
GROUP BY activity_date;
```

## Key Learning

`COUNT(DISTINCT column)` is used when we need to count **unique values**.

`DATE_SUB()` is useful for calculating a date relative to another date. Here, `29 DAY` together with the end date gives a **30-day inclusive range**.
