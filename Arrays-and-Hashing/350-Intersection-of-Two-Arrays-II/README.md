# Intersection of Two Arrays II — LeetCode #350

## 🧠 Pattern
HashMap / Frequency Map

## 💡 Intuition
Count how many times each number appears in the first array.
Then use those counts to find the common elements in the second array.

## 🔍 Approach
1. Create a dictionary to store the frequency of each number in `nums1`.
2. Traverse `nums2`.
3. If the number exists and its count is greater than 0, add it to the result.
4. Decrease its count by 1.
5. Return the result.

## 🐍 Python Concepts
- Dictionary
- `dict.get()`
- `in`
- `if`
- List `.append()`
- `-= 1`
- Frequency counting

## ⏱️ Complexity
- Time: O(n + m)
- Space: O(n)

## 🔑 Key Learning
A frequency map can track how many times an element is available and prevent using it more times than it occurs.
