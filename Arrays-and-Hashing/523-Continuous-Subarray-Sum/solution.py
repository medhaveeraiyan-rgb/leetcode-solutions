class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        count=[]
        sum=[]
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            sum.append(prefix)
        remainder = {0: -1}

        for i in range(len(sum)):
            rem = sum[i] % k

            if rem in remainder:
                if i - remainder[rem] >= 2:
                    return True
            else:
                remainder[rem] = i

        return False
