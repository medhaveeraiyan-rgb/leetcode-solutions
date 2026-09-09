# Biggest Single Number — LeetCode #619

## Intuition

We need to find the **largest number that appears exactly once** in the `MyNumbers` table.

First, group the numbers and keep only the numbers whose count is `1`. Then, from those unique numbers, find the maximum value.

## Approach

1. Use `GROUP BY num` to group identical numbers.
2. Use `HAVING COUNT(num) = 1` to keep only numbers that appear exactly once.
3. Use `MAX(num)` to find the largest number among the unique numbers.
4. The subquery is given the alias `UniqueNumbers` because MySQL requires a name for a derived table.

## Complexity

* Time complexity: **O(n)**
* Space complexity: **O(n)**

## Code

```mysql
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) AS UniqueNumbers;
```

## Key Learning

`GROUP BY` groups duplicate values, `HAVING` filters the groups, and `MAX()` can then find the largest value from the remaining rows.
