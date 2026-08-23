class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        c = {}

        for i in nums:
            c[i] = c.get(i, 0) + 1

        for i in nums:
            if c[i] > n / 2:
                return i
