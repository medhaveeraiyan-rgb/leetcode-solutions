# Intuition

I used a dictionary to keep track of how many times each number appears in the array.

If a number appears exactly twice, it is a duplicate, so I add it to the result array.

# Approach

1. Create an empty dictionary `result` to store the frequency of each number.
2. Traverse through `nums` and increase the count of each number using `get()`.
3. Traverse through the dictionary.
4. If the frequency of a number is `2`, add that number to the result array.
5. Return the result array.

# Complexity

* Time complexity: `O(n)`
* Space complexity: `O(n)`

# Code

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = dict()
        array = []

        for i in nums:
            result[i] = result.get(i, 0) + 1

        for i in result:
            if result[i] == 2:
                array.append(i)

        return array
```
