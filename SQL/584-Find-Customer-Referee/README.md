# Find Customer Referee — LeetCode #584

## Intuition

We need to find customers who were not referred by customer 2.
Customers who have no referee should also be included.

## Approach

Select the customer names from the Customer table.
Filter customers whose referee_id is not 2 or whose referee_id is NULL.
Use IS NULL because NULL cannot be compared using normal comparison operators.

## SQL Concepts

- SELECT
- FROM
- WHERE
- OR
- <>
- NULL
- IS NULL

## Complexity

Time: O(n)

Space: O(1)

## Key Learning

NULL must be checked using IS NULL instead of = NULL.

## Solution

```sql
SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id IS NULL;
