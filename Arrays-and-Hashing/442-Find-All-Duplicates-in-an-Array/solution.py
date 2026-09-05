class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result=dict()
        array=[]
        for i in nums:
            result[i]= result.get(i,0)+1
        for i in result:
            if result[i]==2:
                array.append(i)
        return array
