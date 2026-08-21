# Contains Duplicate — LeetCode #217

## 🧠 Pattern
Set / Uniqueness

## 💡 Intuition
A set stores only unique values.
If the length of the original array and the set are different, duplicates exist.

## 🔍 Approach
1. Convert the array into a set.
2. Compare the lengths of the array and set.
3. If the lengths are different, return `True`.
4. Otherwise, return `False`.

## 🐍 Python Concepts
- List
- `set()`
- `len()`
- `if-else`
- Comparing values

## ⏱️ Complexity
- Time: O(n)
- Space: O(n)

## 🔑 Key Learning
Use a set when you need to check uniqueness or detect duplicates.
