# Replace Employee ID With The Unique Identifier — LeetCode #1378

## Intuition

We need to display each employee's name along with their unique ID.
The Employees and EmployeeUNI tables are connected using the employee id.
We use a LEFT JOIN so that every employee is included, even if they do not have a unique ID.

## Approach

1. Select unique_id from EmployeeUNI and name from Employees.
2. Join the two tables using their common id column.
3. Use LEFT JOIN to keep all employees.
4. Employees without a matching unique ID will have NULL.

## SQL Concepts

- SELECT
- FROM
- LEFT JOIN
- ON
- Table Aliases
- NULL

## Complexity

Time: O(n)

Space: O(n)

## Key Learning

LEFT JOIN keeps every row from the left table even when there is no matching row in the right table.

## Solution

```sql
SELECT eu.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
    ON e.id = eu.id;
