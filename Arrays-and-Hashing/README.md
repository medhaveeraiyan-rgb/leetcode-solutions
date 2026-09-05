# 🧠 Arrays & Hashing

This section focuses on fundamental array and hash-based problem-solving patterns.

The main goal is to learn how to use **arrays, sets, dictionaries, frequency counting, prefix sums, and hashing techniques** to solve problems efficiently.

## 📊 Progress

**14 / 14 Completed ✅**

| #   | Problem                                                                   | Pattern               | Status |
| --- | ------------------------------------------------------------------------- | --------------------- | ------ |
| 1   | [Two Sum](./001-Two-Sum/)                                                 | HashMap               | ✅      |
| 49  | [Group Anagrams](./049-Group-Anagrams/)                                   | HashMap + Sorting     | ✅      |
| 128 | [Longest Consecutive Sequence](./128-Longest-Consecutive-Sequence/)       | HashSet               | ✅      |
| 169 | [Majority Element](./169-Majority-Element/)                               | HashMap               | ✅      |
| 217 | [Contains Duplicate](./217-Contains-Duplicate/)                           | HashSet               | ✅      |
| 238 | [Product of Array Except Self](./238-Product-of-Array-Except-Self/)       | Prefix/Suffix Product | ✅      |
| 242 | [Valid Anagram](./242-Valid-Anagram/)                                     | Frequency Counting    | ✅      |
| 268 | [Missing Number](./268-Missing-Number/)                                   | Math                  | ✅      |
| 347 | [Top K Frequent Elements](./347-Top-K-Frequent-Elements/)                 | HashMap + Heap        | ✅      |
| 350 | [Intersection of Two Arrays II](./350-Intersection-of-Two-Arrays-II/)     | HashMap               | ✅      |
| 442 | [Find All Duplicates in an Array](./442-Find-All-Duplicates-in-an-Array/) | HashMap               | ✅      |
| 523 | [Continuous Subarray Sum](./523-Continuous-Subarray-Sum/)                 | Prefix Sum + HashMap  | ✅      |
| 560 | [Subarray Sum Equals K](./560-Subarray-Sum-Equals-K/)                     | Prefix Sum + HashMap  | ✅      |

## 🔑 Patterns Learned

### 1. HashMap / Dictionary

Used to store values and their frequencies or positions.

Problems:

* Two Sum
* Contains Duplicate
* Valid Anagram
* Majority Element
* Intersection of Two Arrays II
* Find All Duplicates in an Array

### 2. HashSet

Used when we mainly need to check whether a value exists.

Problem:

* Longest Consecutive Sequence

### 3. Frequency Counting

Count how many times each value appears.

Problems:

* Valid Anagram
* Majority Element
* Top K Frequent Elements
* Find All Duplicates in an Array

### 4. Prefix Sum

Keep a running sum to efficiently reason about subarray sums.

Problems:

* Subarray Sum Equals K
* Continuous Subarray Sum

### 5. Sorting

Use sorting to group or compare elements.

Problem:

* Group Anagrams

### 6. Prefix & Suffix

Calculate information from both directions of an array.

Problem:

* Product of Array Except Self

## 💡 Key Lessons

* Use a **HashMap** when you need fast lookup or frequency counting.
* Use a **HashSet** when you mainly need fast existence checking.
* Use **Prefix Sum** for many subarray-sum problems.
* Always think about the required **time and space complexity**.
* Try to identify the pattern before writing the code.

## 🚀 Next Section

**Two Pointers & Sliding Window**

The next stage will focus on:

* Two Pointers
* Sliding Window
* Maintaining a valid window
* Efficient array/string traversal

---

### Progress

**Arrays & Hashing: 14/14 ✅**

**Next → Two Pointers & Sliding Window 🔥**
