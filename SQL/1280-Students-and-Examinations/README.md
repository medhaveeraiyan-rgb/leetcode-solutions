# Students and Examinations — LeetCode #1280

## Intuition

We need to find the number of exams attended by each student for every subject.

First, create every possible combination of students and subjects using `CROSS JOIN`. Then use `LEFT JOIN` with the `Examinations` table to find the exams attended by each student for each subject. Finally, use `COUNT()` to count the exams.

## Approach

1. Use `CROSS JOIN` between `Students` and `Subjects` to create every student-subject combination.
2. Use `LEFT JOIN` with `Examinations` using both `student_id` and `subject_name`.
3. Use `COUNT()` to count the examinations for each student and subject.
4. Use `GROUP BY` to create one group for each student-subject combination.
5. Use `ORDER BY` to sort by `student_id` and `subject_name`.

## Complexity

* Time complexity: **O(S × U + E)**, where `S` is the number of students, `U` is the number of subjects, and `E` is the number of examination records.
* Space complexity: **O(S × U)** for the intermediate student-subject combinations.

## Code

```mysql
# Write your MySQL query statement below

SELECT 
    s.student_id,
    s.student_name,
    su.subject_name,
    COUNT(e.subject_name) AS attended_exams

FROM Students s

-- Create every possible student + subject combination
CROSS JOIN Subjects su

-- Find exams attended by that student for that subject
LEFT JOIN Examinations e
    ON e.student_id = s.student_id
    AND e.subject_name = su.subject_name

-- Group each student and subject together
GROUP BY 
    s.student_id,
    s.student_name,
    su.subject_name

-- Sort the result
ORDER BY 
    s.student_id,
    su.subject_name;
```

## Key Learning

`CROSS JOIN` creates all student-subject combinations, while `LEFT JOIN + COUNT()` helps count exams even when a student attended **0 exams** for a subject.

````

### GitHub

Create:

```text
SQL/
└── 1280-Students-and-Examinations/
    ├── solution.sql
    └── README.md
````

**`solution.sql`** → put the SQL code above.

**`README.md`** → put the write-up above.

Then commit:

```bash
git add .
git commit -m "Add LeetCode 1280 Students and Examinations"
git push
```

This one is a good problem to keep because it teaches the very important **CROSS JOIN + LEFT JOIN + GROUP BY + COUNT** pattern.
