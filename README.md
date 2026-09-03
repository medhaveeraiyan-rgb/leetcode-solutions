# 🧠 LeetCode Solutions

Welcome to my **LeetCode problem-solving journey**.

This repository contains my solutions, explanations, and notes as I work through **Data Structures & Algorithms** and **SQL** problems.

> **Learn → Understand → Solve → Analyze → Document → Repeat**

The goal is not just to collect accepted solutions, but to understand the **patterns and concepts behind every problem**.

---

## 📊 Progress

| Track               | Problems Solved | Status         |
| ------------------- | --------------: | -------------- |
| 🔢 Arrays & Hashing |          **10** | 🟢 In Progress |
| 🗄️ SQL             |     **15 / 50** | 🟢 30%         |
| 🏆 SQL 50           |     **15 / 50** | 🟢 In Progress |

---

## 🗂️ Repository Structure

```text
leetcode-solutions/
│
├── Arrays-and-Hashing/
│   ├── 001-Two-Sum/
│   ├── 049-Group-Anagrams/
│   ├── 128-Longest-Consecutive-Sequence/
│   ├── 169-Majority-Element/
│   ├── 217-Contains-Duplicate/
│   ├── 238-Product-of-Array-Except-Self/
│   ├── 242-Valid-Anagram/
│   ├── 268-Missing-Number/
│   ├── 347-Top-K-Frequent-Elements/
│   └── 350-Intersection-of-Two-Arrays-II/
│
├── SQL/
│   ├── 1068-Product-Sales-Analysis-I/
│   ├── 1075-Project-Employees-I/
│   ├── 1148-Article-Views-I/
│   ├── 1251-Average-Selling-Price/
│   ├── 1378-Replace-Employee-ID-With-The-Unique-Identifier/
│   ├── 1581-Customer-Who-Visited-but-Did-Not-Make-Any-Transactions/
│   ├── 1633-Percentage-of-Users-Attended-a-Contest/
│   ├── 1661-Average-Time-of-Process-per-Machine/
│   ├── 1683-Invalid-Tweets/
│   ├── 1757-Recyclable-and-Low-Fat-Products/
│   ├── 197-Rising-Temperature/
│   ├── 577-Employee-Bonus/
│   ├── 584-Find-Customer-Referee/
│   ├── 595-Big-Countries/
│   ├── 620-Not-Boring-Movies/
│   └── README.md
│
└── README.md
```

---

# 🔢 Arrays & Hashing

My DSA journey begins with **Arrays & Hashing**, focusing on building strong problem-solving fundamentals and recognizing common patterns.

### 🎯 Focus Areas

* Arrays
* Hashing
* Hash Maps
* Hash Sets
* Frequency Counting
* Searching
* Array Manipulation
* Problem-solving patterns

### ✅ Solved

|   # | Problem                       | Difficulty | Main Concept         |
| --: | ----------------------------- | :--------: | -------------------- |
|   1 | Two Sum                       |    Easy    | Hash Map             |
|  49 | Group Anagrams                |   Medium   | Hash Map / Frequency |
| 128 | Longest Consecutive Sequence  |   Medium   | Hash Set             |
| 169 | Majority Element              |    Easy    | Hash Map             |
| 217 | Contains Duplicate            |    Easy    | Hash Set             |
| 238 | Product of Array Except Self  |   Medium   | Prefix / Suffix      |
| 242 | Valid Anagram                 |    Easy    | Frequency Counting   |
| 268 | Missing Number                |    Easy    | Array / Math         |
| 347 | Top K Frequent Elements       |   Medium   | Hash Map / Heap      |
| 350 | Intersection of Two Arrays II |    Easy    | Hash Map             |

---

# 🗄️ SQL

I am learning **SQL from absolute zero** and following the **LeetCode SQL 50** study plan.

The focus is on developing strong **SQL and DBMS fundamentals** for technical interviews, placements, and real-world database problem solving.

### 🎯 Learning Path

```text
SQL Fundamentals
       ↓
Functions & Aggregation
       ↓
Joins
       ↓
Subqueries
       ↓
Intermediate SQL
       ↓
Advanced SQL
       ↓
Interview Patterns
```

### 🏆 SQL 50 Progress

**15 / 50**

`██████░░░░░░░░░░░░` **30%**

### ✅ Solved

|    # | Problem                                                | Difficulty | Main Concepts       |
| ---: | ------------------------------------------------------ | :--------: | ------------------- |
| 1068 | Product Sales Analysis I                               |    Easy    | JOIN, Foreign Key   |
| 1075 | Project Employees I                                    |    Easy    | JOIN, AVG, GROUP BY |
| 1148 | Article Views I                                        |    Easy    | DISTINCT, WHERE     |
| 1251 | Average Selling Price                                  |    Easy    | JOIN, SUM, ROUND    |
| 1378 | Replace Employee ID With The Unique Identifier         |    Easy    | LEFT JOIN           |
| 1581 | Customer Who Visited but Did Not Make Any Transactions |    Easy    | LEFT JOIN, NULL     |
| 1633 | Percentage of Users Attended a Contest                 |    Easy    | GROUP BY, Subquery  |
| 1661 | Average Time of Process per Machine                    |   Medium   | SELF JOIN, AVG      |
| 1683 | Invalid Tweets                                         |    Easy    | CHAR_LENGTH         |
| 1757 | Recyclable and Low Fat Products                        |    Easy    | SELECT, WHERE       |
|  197 | Rising Temperature                                     |    Easy    | SELF JOIN           |
|  577 | Employee Bonus                                         |    Easy    | LEFT JOIN, NULL     |
|  584 | Find Customer Referee                                  |    Easy    | NULL, OR            |
|  595 | Big Countries                                          |    Easy    | WHERE, OR           |
|  620 | Not Boring Movies                                      |    Easy    | ORDER BY, Modulo    |

---

## 🧠 SQL Concepts

### Fundamentals

* [x] SELECT
* [x] FROM
* [x] WHERE
* [x] Comparison Operators
* [x] AND / OR / NOT
* [x] NULL
* [x] IS NULL / IS NOT NULL
* [x] DISTINCT
* [x] ORDER BY
* [x] LIMIT
* [x] IN
* [x] BETWEEN
* [ ] LIKE
* [ ] NOT IN

### Functions & Aggregation

* [x] COUNT()
* [x] SUM()
* [x] AVG()
* [x] GROUP BY
* [x] ROUND()
* [x] COALESCE()
* [ ] MIN()
* [ ] MAX()
* [ ] HAVING

### Joins

* [x] INNER JOIN
* [x] LEFT JOIN
* [x] SELF JOIN
* [ ] RIGHT JOIN
* [x] Primary Key & Foreign Key
* [x] Multiple-table Queries

### Intermediate SQL

* [x] CASE
* [x] Subqueries
* [x] IN with Subqueries
* [ ] EXISTS
* [ ] NOT EXISTS
* [ ] UNION
* [ ] UNION ALL
* [x] NULL Handling

### Advanced SQL

* [ ] CTEs
* [ ] Window Functions
* [ ] ROW_NUMBER()
* [ ] RANK()
* [ ] DENSE_RANK()
* [ ] PARTITION BY

---

# 📝 How I Solve

For every problem, I follow a consistent process:

```text
01. Understand the Problem
          ↓
02. Identify the Pattern
          ↓
03. Think of the Solution
          ↓
04. Solve Independently
          ↓
05. Analyze Complexity
          ↓
06. Document the Approach
          ↓
07. Commit to GitHub
```

Each problem folder contains:

```text
Problem/
├── solution
└── README.md
```

The README generally includes:

* Intuition
* Approach
* Concepts Used
* Complexity
* Key Learning

---

# 🎯 Goals

* [ ] Complete LeetCode SQL 50
* [ ] Build strong SQL & DBMS fundamentals
* [ ] Complete core DSA patterns
* [ ] Improve problem-solving speed
* [ ] Prepare for technical interviews
* [ ] Maintain consistent GitHub activity
* [ ] Build a strong foundation for placement coding rounds

---

# 📈 What's Next?

### 🔢 DSA

Continue strengthening:

```text
Arrays & Hashing
      ↓
Two Pointers
      ↓
Sliding Window
      ↓
Stack
      ↓
Binary Search
      ↓
Linked List
      ↓
Trees
      ↓
Graphs
      ↓
Dynamic Programming
```

### 🗄️ SQL

Continue with:

```text
Aggregation
    ↓
HAVING
    ↓
Subqueries
    ↓
EXISTS
    ↓
UNION
    ↓
CTEs
    ↓
Window Functions
    ↓
Interview SQL Patterns
```

---

## 🚀 Learning Philosophy

> **Consistency over speed.**

Every accepted solution is not just another problem solved — it is another pattern understood.

This repository documents that journey.
