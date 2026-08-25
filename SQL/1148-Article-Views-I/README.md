# Article Views I — LeetCode #1148

## Intuition

We need to find authors who viewed their own articles.
So, we find rows where the author_id and viewer_id are the same.

## Approach

1. Select author_id and rename it as id.
2. Use DISTINCT to remove duplicate authors.
3. Filter rows where author_id = viewer_id.
4. Sort the result by author_id in ascending order.

## SQL Concepts

- SELECT
- DISTINCT
- AS
- WHERE
- ORDER BY
- ASC

## Complexity

Time: O(n log n)

Space: O(n)

## Key Learning

DISTINCT removes duplicate values from the result.

## Solution

```sql
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id ASC;
