class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            if i%3!=0 :
                s+=1
        return s