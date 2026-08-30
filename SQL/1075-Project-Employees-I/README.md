# Intuition

We need to find the average experience of employees working on each project.
The `Project` and `Employee` tables are connected using `employee_id`, so we join them and calculate the average experience for each project.

# Approach

1. Join `Project` with `Employee` using `employee_id`.
2. Group the employees by `project_id`.
3. Calculate the average experience using `AVG()`.
4. Round the average to 2 decimal places using `ROUND()`.

# Complexity

* Time: O(n)
* Space: O(n)

# Code

```sql
SELECT p.project_id,
       ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project p
LEFT JOIN Employee e
    ON p.employee_id = e.employee_id
GROUP BY p.project_id;
```

## Key Learning

`GROUP BY` lets us calculate aggregate values such as `AVG()` separately for each project.
