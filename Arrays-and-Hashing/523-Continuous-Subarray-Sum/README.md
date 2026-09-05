# Intuition

I used the **Prefix Sum + HashMap** approach.

I calculate the prefix sum while traversing the array and find its remainder when divided by `k`.

If the same remainder has appeared before, the sum of the elements between those two positions is divisible by `k`.

I also store the index where each remainder first appeared so that I can check whether the subarray contains at least 2 elements.

# Approach

1. Calculate the running prefix sum.
2. Calculate the remainder of the prefix sum using `prefix % k`.
3. Store each remainder with the index where it first appeared.
4. If the same remainder appears again, calculate the distance between the current index and the previous index.
5. If the distance is at least `2`, return `True`.
6. Initialize `remainder = {0: -1}` to handle subarrays starting from index `0`.
7. If no valid subarray is found, return `False`.

# Complexity

* Time complexity: `O(n)`
* Space complexity: `O(n)`

# Code

```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        remainder = {0: -1}

        for i in range(len(nums)):
            prefix += nums[i]
            rem = prefix % k

            if rem in remainder:
                if i - remainder[rem] >= 2:
                    return True
            else:
                remainder[rem] = i

        return False
```
