# Valid Anagram — LeetCode #242

## 🧠 Pattern
HashMap / Dictionary + Frequency Counting

## 💡 Intuition
Two strings are anagrams if they contain the same characters with the same frequencies.

## 🔍 Approach
1. Check if both strings have the same length.
2. Create a dictionary for each string.
3. Count how many times each character appears.
4. Compare both dictionaries.
5. If they are equal, return `True`.

## 🐍 Python Concepts
- Dictionary
- Key-value pairs
- `dict.get()`
- `for` loop
- `len()`
- Frequency counting

## ⏱️ Complexity
- Time: O(n)
- Space: O(n)

## 🔑 Key Learning
Use a dictionary to count the frequency of elements when their occurrences matter.
