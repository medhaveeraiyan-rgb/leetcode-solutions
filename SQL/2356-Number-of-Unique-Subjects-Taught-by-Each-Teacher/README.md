# Number of Unique Subjects Taught by Each Teacher — LeetCode #2356

## Intuition

We need to find how many **different subjects** each teacher teaches.

A teacher may appear multiple times for the same subject, so we use `COUNT(DISTINCT subject_id)` to count each subject only once.

## Approach

1. Select the `teacher_id`.
2. Count the unique subjects using `COUNT(DISTINCT subject_id)`.
3. Group the records by `teacher_id`.
4. Store the result as `cnt`.

## Complexity

* Time complexity: **O(n)**
* Space complexity: **O(n)**

## Code

```mysql
# Write your MySQL query statement below

SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
```

## Key Learning

`COUNT(DISTINCT column)` counts only the unique values in a column, while `GROUP BY` performs the calculation separately for each teacher.
