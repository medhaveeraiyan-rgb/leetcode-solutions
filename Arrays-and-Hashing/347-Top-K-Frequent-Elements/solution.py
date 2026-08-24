class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for i in nums:
            res[i] = res.get(i, 0) + 1

        sorted_num = sorted(res, key=res.get, reverse=True)

        return sorted_num[:k]
