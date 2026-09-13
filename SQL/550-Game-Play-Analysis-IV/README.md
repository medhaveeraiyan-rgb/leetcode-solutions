# Game Play Analysis IV — LeetCode #550

## Intuition

We need to find the fraction of players who **logged in again exactly one day after their first login**.

For each player, first find their earliest login date. Then check whether that player has a login on the following day.

## Approach

1. Find each player's first login date using `MIN(event_date)`.
2. Group the records by `player_id` to get one first-login date per player.
3. Join this result back with the `Activity` table.
4. Use `DATE_ADD()` to calculate the day after the first login.
5. Count the distinct players who logged in on that next day.
6. Divide this count by the total number of distinct players.
7. Round the resulting fraction to 2 decimal places.

## Complexity

* Time complexity: **O(n)**
* Space complexity: **O(n)**

## Code

```mysql id="q7m2kd"
# Write your MySQL query statement below

SELECT 
    ROUND(
        COUNT(DISTINCT a1.player_id) / 
        (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction
FROM Activity a1
JOIN (
    SELECT 
        player_id, 
        MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) a2 
    ON a1.player_id = a2.player_id 
    AND a1.event_date = DATE_ADD(a2.first_login, INTERVAL 1 DAY);
```

## Key Learning

`MIN()` with `GROUP BY` is useful for finding the **first record for each user**.

`DATE_ADD()` can be used to check whether an event happened a specific number of days after another date.

The pattern **count matching users / total users** is useful for calculating fractions and percentages.
