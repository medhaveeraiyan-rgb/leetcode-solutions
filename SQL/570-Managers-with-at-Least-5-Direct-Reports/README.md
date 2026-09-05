# Managers with at Least 5 Direct Reports — LeetCode #570

## Intuition

We need to find managers who have at least 5 employees directly reporting to them.

We can first find the `managerId` values that appear at least 5 times using `GROUP BY` and `HAVING`. Then use a subquery with `IN` to find the names of those managers.

## Approach

1. Group employees by `managerId`.
2. Use `HAVING COUNT(id) >= 5` to find managers with at least 5 direct reports.
3. Use a subquery to get these `managerId` values.
4. Use `IN` in the main query to find the corresponding manager names.

## Complexity

* Time complexity: **O(n)**
* Space complexity: **O(n)**

## Code

```mysql
# Write your MySQL query statement below

SELECT name
FROM Employee 
WHERE id IN (
    SELECT managerId
    FROM Employee 
    GROUP BY managerId
    HAVING COUNT(id) >= 5
);
```

## Key Learning

`GROUP BY` groups employees by manager, `HAVING` filters the groups, and `IN` lets the main query find the matching managers.
