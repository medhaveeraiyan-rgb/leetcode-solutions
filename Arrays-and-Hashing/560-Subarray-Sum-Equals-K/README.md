# Intuition

A subarray is a continuous part of an array.

To find subarrays whose sum is equal to `k`, I use **Prefix Sum + HashMap**.

For every position, I calculate the current prefix sum. If the current prefix sum is `sums`, then I need a previous prefix sum of:

`sums - k`

If that prefix sum has appeared before, then the elements between those two positions have sum `k`.

I store each prefix sum and its frequency in a dictionary.

# Approach

1. Initialize `count = 0` to store the number of valid subarrays.
2. Initialize `sums = 0` to store the current prefix sum.
3. Use a dictionary `d` to store prefix sums and their frequencies.
4. Set `d[0] = 1` to handle subarrays that start from index `0`.
5. Traverse the array:

   * Add the current number to `sums`.
   * Check whether `sums - k` exists in the dictionary.
   * If it exists, add its frequency to `count`.
   * Store the current prefix sum in the dictionary.
6. Return `count`.

# Complexity

* Time complexity: `O(n)`
* Space complexity: `O(n)`

# Code

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        d = dict()
        d[0] = 1

        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums - k, 0)
            d[sums] = d.get(sums, 0) + 1

        return count
```
