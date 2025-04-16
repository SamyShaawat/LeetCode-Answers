class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        res = 0  
        left = 0 
        # Total number of good pairs (i < j and nums[i] == nums[j]) in the current window
        pairs = 0 
        # Frequency counter for elements in the current window
        counter = Counter() 
        n = len(nums)               
        
        # Expand the window to the right
        for right in range(n):      
            # Adding the number of existing elements equal to nums[right] 
            pairs += counter[nums[right]]  
            # Increase the frequency of nums[right] in the window
            counter[nums[right]] += 1         
            
            # If current window has at least k good pairs
            while pairs >= k:       
                # We're going to shrink the window from the left, so decrease count of nums[left]
                counter[nums[left]] -= 1      
                # Remove pairs that nums[left] was contributing to (after decrementing its count)
                pairs -= counter[nums[left]]  
                # Shrink the window by moving the left pointer right
                left += 1                     

            # Add the number of valid starting points for subarrays ending at `right`
            res += left    
        return res               
