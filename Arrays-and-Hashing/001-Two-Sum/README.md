# Two Sum — LeetCode #1

## 🧠 Pattern
Array Traversal / Nested Loops

## 💡 Intuition
Check every possible pair of numbers and find the two numbers whose sum equals the target.

## 🔍 Approach
Use two loops to check each pair.
Start the second loop from `i + 1` so that:
- We don't use the same element twice.
- We don't check the same pair again.

## 🐍 Python Concepts
- Lists
- Indexing
- `len()`
- `range()`
- `for` loop
- Nested loops
- `return`

## ⏱️ Complexity
- Time: O(n²)
- Space: O(1)

## 🔑 Key Learning
Use nested loops when we need to check every possible pair.
