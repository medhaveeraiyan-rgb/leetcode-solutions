# Top K Frequent Elements — LeetCode #347

## 🧠 Pattern
HashMap / Frequency Counting + Sorting

## 💡 Intuition
Count how many times each number appears, then sort the numbers based on their frequencies and take the first `k` elements.

## 🔍 Approach
1. Create a dictionary to store the frequency of each number.
2. Count every number using `dict.get()`.
3. Sort the dictionary keys based on their frequency in descending order.
4. Return the first `k` numbers.

## 🐍 Python Concepts
- Dictionary
- `dict.get()`
- `sorted()`
- `key=`
- `reverse=True`
- List slicing `[:k]`

## ⏱️ Complexity
- Time: O(n log n)
- Space: O(n)

## 🔑 Key Learning
A dictionary can store frequencies, and `sorted()` can use those frequencies as the sorting key.
