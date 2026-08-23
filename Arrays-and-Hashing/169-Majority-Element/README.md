# Majority Element — LeetCode #169

## 🧠 Pattern
HashMap / Frequency Counting

## 💡 Intuition
Count how many times each number appears.
The majority element is the number that appears more than `n / 2` times.

## 🔍 Approach
1. Find the length of the array.
2. Use a dictionary to count the frequency of each number.
3. Traverse the numbers and check their frequency.
4. Return the number whose count is greater than `n / 2`.

## 🐍 Python Concepts
- Dictionary
- `dict.get()`
- `for` loop
- `len()`
- Comparison operators
- Frequency counting

## ⏱️ Complexity
- Time: O(n)
- Space: O(n)

## 🔑 Key Learning
Use a frequency map when you need to find an element based on how many times it appears.
