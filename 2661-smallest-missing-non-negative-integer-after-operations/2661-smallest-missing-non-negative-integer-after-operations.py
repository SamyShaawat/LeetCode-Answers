class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n=len(nums)
        mod=[0]*value
        for x in nums:
            x%=value
            if x<0: x+=value
            mod[x]+=1
        for i in range(n):
            j=i%value
            mod[j]-=1
            if (mod[j]<0): return i
        return n
        