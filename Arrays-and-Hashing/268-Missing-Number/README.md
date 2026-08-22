# Missing Number — LeetCode #268

## 🧠 Pattern
Array Traversal / Searching

## 💡 Intuition
The array contains numbers from `0` to `n` with one number missing.
Check each number in this range and find the one that is not present.

## 🔍 Approach
1. Find the length of the array.
2. Loop from `0` to `n`.
3. Check whether each number exists in `nums`.
4. Return the number that is missing.

## 🐍 Python Concepts
- `len()`
- `range()`
- `for` loop
- `in` operator
- `not in` operator
- List traversal

## ⏱️ Complexity
- Time: O(n²)
- Space: O(1)

## 🔑 Key Learning
Use `not in` to check whether an element is absent from a list.
