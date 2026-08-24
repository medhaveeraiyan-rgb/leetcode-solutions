# Big Countries — LeetCode #595

## Intuition

We need to find countries that are big based on either their area or population.
A country is considered big if its area is at least 3,000,000 or its population is at least 25,000,000.

## Approach

Select the name, population, and area from the World table.
Use WHERE with OR to keep countries that satisfy either condition.

## SQL Concepts

- SELECT
- FROM
- WHERE
- OR
- >=

## Complexity

Time: O(n)

Space: O(1)

## Key Learning

OR is used when at least one of multiple conditions can be true.

## Solution

```sql
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;
