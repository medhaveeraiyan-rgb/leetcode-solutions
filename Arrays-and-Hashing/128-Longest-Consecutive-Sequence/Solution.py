class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = 0
        l = set(nums)

        for i in l:
            if i - 1 not in l:
                count = 1

                while i + count in l:
                    count += 1

                longest = max(count, longest)

        return longest
