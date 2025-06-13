class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
     
        nums.sort()
        n = len(nums)

        low, high = 0, nums[-1] - nums[0]

      
        while low < high:
            mid = (low + high) // 2

            
            count = 0
            i = 1
            while i < n and count < p:
                if nums[i] - nums[i - 1] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1

     
            if count >= p:
                high = mid
            else:
                low = mid + 1

   
        return low