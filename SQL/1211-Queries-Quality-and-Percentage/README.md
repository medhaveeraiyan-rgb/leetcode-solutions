# Queries Quality and Percentage — LeetCode #1211

## Intuition

We need to calculate two values for each query name: the average quality and the percentage of poor queries.

Quality is calculated using `rating / position`, while a poor query is one where the rating is less than 3.

## Approach

1. Group the records by `query_name`.
2. Calculate the average of `rating / position` using `AVG()`.
3. Round the quality to 2 decimal places.
4. Count queries with `rating < 3` using `CASE`.
5. Divide the number of poor queries by the total number of queries and multiply by 100.
6. Round the poor query percentage to 2 decimal places.

## Complexity

* Time complexity: **O(n)**
* Space complexity: **O(n)**

## Code

```mysql
# Write your MySQL query statement below

SELECT
    query_name,

    -- Calculate the average quality
    ROUND(AVG(CAST(rating AS DECIMAL) / position), 2) AS quality,

    -- Count poor queries (rating < 3),
    -- divide by total queries and convert to percentage
    ROUND(
        SUM(CASE
                WHEN rating < 3 THEN 1
                ELSE 0
            END) * 100 / COUNT(*),
        2
    ) AS poor_query_percentage

FROM Queries

-- Calculate the values separately for each query name
GROUP BY query_name;
```

## Key Learning

`CASE` can be used for conditional counting, while `AVG()`, `COUNT()`, and `GROUP BY` are useful for calculating statistics for each group.
