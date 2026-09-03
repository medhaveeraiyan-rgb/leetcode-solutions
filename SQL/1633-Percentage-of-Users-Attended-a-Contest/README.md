# Percentage of Users Attended a Contest — LeetCode #1633

## Intuition

For each contest, calculate the percentage of registered users out of all users.

We count the users in each contest, divide by the total number of users, multiply by 100, and round to two decimal places.

## Approach

1. Group registrations by `contest_id`.
2. Count registered users using `COUNT(user_id)`.
3. Get the total number of users using a subquery.
4. Calculate the percentage and round it to 2 decimals.
5. Sort by percentage descending and `contest_id` ascending for ties.

## SQL Concepts

* COUNT()
* GROUP BY
* Subquery
* ROUND()
* ORDER BY
* DESC / ASC
* Arithmetic operations

## Complexity

* Time complexity: `O(R)`
* Space complexity: `O(C)`

Where `R` is the number of registration records and `C` is the number of contests.

## Code

```mysql
SELECT contest_id,
       ROUND(
           COUNT(user_id) * 100.0 /
           (SELECT COUNT(*) FROM Users),
           2
       ) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;
```

## Key Learning

A subquery can calculate a value needed by the main query, such as the total number of users.
