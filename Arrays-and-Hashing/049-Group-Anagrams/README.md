# Group Anagrams — LeetCode #49

## 🧠 Pattern
HashMap / Grouping

## 💡 Intuition
Anagrams contain the same characters. Sorting the characters of each word gives the same key for all anagrams.

## 🔍 Approach
1. Create a dictionary where each key stores a list of words.
2. Sort each word's characters to create a key.
3. Add the original word to the list belonging to that key.
4. Return all the grouped values.

## 🐍 Python Concepts
- Dictionary
- `defaultdict(list)`
- `sorted()`
- `"".join()`
- `.append()`
- `.values()`
- `for` loop

## ⏱️ Complexity
- Time: O(n × k log k)
- Space: O(n × k)

## 🔑 Key Learning
A calculated key can be used with a dictionary to group similar items together.
