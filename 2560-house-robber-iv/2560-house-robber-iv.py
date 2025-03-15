class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def possible_robbery(min_cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= min_cap:
                    count += 1
                    i += 1 
                i += 1 
            return count >= k

            
        l=min(nums)
        r=max(nums)
        ans=0
        while l<=r:
            mid= (r + l) // 2

            if possible_robbery(mid):
                ans=mid
                r=mid-1
                
            else:
                l=mid+1
            
        
        return ans