# Intuition

We need to find days when the temperature was higher than the previous day.
We compare each day with the day immediately before it using the record date.

# Approach

1. Use the `Weather` table twice with two aliases, `A` and `B`.
2. Match the dates where `A` is exactly one day after `B`.
3. Check whether `A.temperature` is greater than `B.temperature`.
4. Return the `id` of the warmer day.

# Complexity

* Time: O(n²)
* Space: O(1)

# Code

```sql
SELECT A.id
FROM Weather A, Weather B
WHERE DATEDIFF(A.recordDate, B.recordDate) = 1
  AND A.temperature > B.temperature;
```

## Key Learning

Self-joining a table allows us to compare rows from the same table with each other.
