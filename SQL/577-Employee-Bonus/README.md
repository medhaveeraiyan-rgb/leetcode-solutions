# Employee Bonus — LeetCode #577

## Intuition

We need to find employees who either have **no bonus** or whose bonus is **less than 1000**.

Since some employees may not have a matching row in the `Bonus` table, we use a `LEFT JOIN`.

## Approach

1. Start with the `Employee` table.
2. `LEFT JOIN` the `Bonus` table using `empId`.
3. Keep employees where:

   * bonus is `NULL`, or
   * bonus is less than `1000`.

## SQL Concepts

* LEFT JOIN
* NULL
* IS NULL
* OR
* Table aliases
* WHERE

## Complexity

* Time complexity: `O(E + B)`
* Space complexity: `O(E + B)`

Where `E` is the number of employees and `B` is the number of bonus records.

## Code

```mysql
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b
    ON e.empId = b.empId
WHERE b.bonus IS NULL OR b.bonus < 1000;
```

## Key Learning

`LEFT JOIN` keeps all rows from the left table, even when there is no matching row in the right table. Those unmatched values become `NULL`.
