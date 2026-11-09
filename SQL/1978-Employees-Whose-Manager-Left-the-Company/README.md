# Employees Whose Manager Left the Company — LeetCode #1978

## Intuition

We need to find employees whose salary is less than 30000 and whose manager has left the company.

If a manager has left, their `employee_id` will not exist in the `Employees` table.

We can use `NOT IN` with a subquery to identify such employees.

## Approach

1. Select employees from the `Employees` table.
2. Use `salary < 30000` to filter employees earning less than 30000.
3. Use a subquery to retrieve all existing `employee_id` values.
4. Use `NOT IN` to find employees whose `manager_id` does not exist in the employee list.
5. Use `ORDER BY employee_id` to sort the result in ascending order.

## Complexity

- Time complexity: **O(n)**
- Space complexity: **O(n)**

## Code

```mysql
# Write your MySQL query statement below

SELECT employee_id
FROM Employees
WHERE salary < 30000
  AND manager_id NOT IN (
      SELECT employee_id
      FROM Employees
  )
ORDER BY employee_id;
```

## Key Learning

`NOT IN` is useful for finding values that do not exist in the result of a subquery.

It is commonly used to identify missing relationships between records.
