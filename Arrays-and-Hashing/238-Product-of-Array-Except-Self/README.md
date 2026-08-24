# Product of Array Except Self — LeetCode #238

## 🧠 Pattern
Prefix & Suffix Products

## 💡 Intuition
For each position, the answer is the product of all elements to its left multiplied by the product of all elements to its right.

## 🔍 Approach
1. Traverse from left to right and store the prefix product.
2. Traverse from right to left while maintaining a suffix product.
3. Multiply the prefix and suffix products to get the final answer.

## 🐍 Python Concepts
- Lists
- `range()`
- Forward traversal
- Reverse traversal
- Prefix product
- Suffix product

## ⏱️ Complexity
- Time: O(n)
- Space: O(1) extra space

## 🔑 Key Learning
Instead of using nested loops, calculate the left and right products separately to solve the problem in O(n) time.
