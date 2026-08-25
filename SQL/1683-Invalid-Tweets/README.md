# Invalid Tweets — LeetCode #1683

## Intuition

We need to find tweets whose content contains more than 15 characters.
So, we calculate the length of each tweet's content and filter those greater than 15.

## Approach

1. Select tweet_id from the Tweets table.
2. Use CHAR_LENGTH(content) to calculate the number of characters.
3. Keep tweets whose content length is greater than 15.

## SQL Concepts

- SELECT
- FROM
- WHERE
- CHAR_LENGTH()
- Comparison operator (>)

## Complexity

Time: O(n)

Space: O(1)

## Key Learning

CHAR_LENGTH() can be used to find the number of characters in a string.

## Solution

```sql
SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;
