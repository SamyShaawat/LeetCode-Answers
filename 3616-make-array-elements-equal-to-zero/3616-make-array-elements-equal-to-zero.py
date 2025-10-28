class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prefix, cnt=0, 0
        Sum=sum(nums)
        for x in nums:
            prefix+=x
            if x==0:
                cnt+=2*(2*prefix==Sum)
                cnt+=(abs(2*prefix-Sum)==1)
        return cnt