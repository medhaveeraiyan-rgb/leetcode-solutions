# Longest Consecutive Sequence — LeetCode #128

## Intuition

The goal is to find the length of the longest sequence of consecutive numbers.

I use a set so that I can quickly check whether a number exists.

A number is the start of a sequence if the previous number (`num - 1`) is not present in the set. From that starting number, I keep checking the next consecutive numbers and count their length.

## Approach

1. Convert the array into a set for fast lookup.
2. Iterate through each number in the set.
3. Check whether `num - 1` exists.
4. If it does not exist, the current number is the start of a sequence.
5. Use a while loop to check the next consecutive numbers.
6. Track the maximum sequence length.
7. Return the maximum length.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

## Key Learning

Use a Hash Set to efficiently detect the start and length of consecutive sequences.
