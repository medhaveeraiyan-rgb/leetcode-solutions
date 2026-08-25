# Not Boring Movies — LeetCode #620

## Intuition

We need to find movies that are not boring and have an odd-numbered id.
So, we filter the movies using both conditions and sort them by rating from highest to lowest.

## Approach

1. Select all columns from the Cinema table.
2. Exclude movies whose description is 'boring'.
3. Use `id % 2 = 1` to select movies with odd-numbered IDs.
4. Sort the result by rating in descending order.

## SQL Concepts

- SELECT *
- FROM
- WHERE
- AND
- !=
- Modulo (%)
- ORDER BY
- DESC

## Complexity

Time: O(n log n)

Space: O(1)

## Key Learning

The modulo operator `%` can be used to identify odd and even numbers.

## Solution

```sql
SELECT *
FROM Cinema
WHERE description != 'boring'
  AND id % 2 = 1
ORDER BY rating DESC;
