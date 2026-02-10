class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n=len(nums)
        seen=set()
        Len=0
        for l in range(n):
            if l>n-Len: break # add this line
            diff=0
            for r in range(l, n):
                x=nums[r]
                if x not in seen:
                    diff+=1-(x&1)*2
                    seen.add(x)
                if diff==0:
                    Len=max(Len, r-l+1)
            seen.clear()
        return Len
        