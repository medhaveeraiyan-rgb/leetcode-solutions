class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res1 = {}
        res2 = []

        for i in nums1:
            res1[i] = res1.get(i, 0) + 1

        for i in nums2:
            if i in res1 and res1[i] > 0:
                res2.append(i)
                res1[i] -= 1

        return res2
