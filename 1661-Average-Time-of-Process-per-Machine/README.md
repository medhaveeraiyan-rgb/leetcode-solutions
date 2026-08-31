# Average Time of Process per Machine — LeetCode #1661

## Intuition

Each process has two rows: one for `start` and one for `end`.
We compare these rows by joining the `Activity` table with itself, then calculate the processing time and average it for each machine.

## Approach

1. Use a self join on the `Activity` table.
2. Match rows having the same `machine_id` and `process_id`.
3. Keep the `start` row as `A` and the `end` row as `B`.
4. Calculate the processing time as `B.timestamp - A.timestamp`.
5. Use `AVG()` to calculate the average processing time for each machine.
6. Round the result to 3 decimal places.

## Complexity

* Time: O(n²)
* Space: O(n)

## SQL Concepts

* SELF JOIN
* JOIN
* AVG()
* GROUP BY
* ROUND()
* Table Aliases
* Date/Time difference using timestamps

## Key Learning

A self join can pair related rows from the same table so that values from those rows can be compared or calculated together.

## Code

```sql
SELECT A.machine_id,
       ROUND(AVG(B.timestamp - A.timestamp), 3) AS processing_time
FROM Activity A
JOIN Activity B
    ON A.machine_id = B.machine_id
    AND A.process_id = B.process_id
WHERE A.activity_type = 'start'
  AND B.activity_type = 'end'
GROUP BY A.machine_id;
```
