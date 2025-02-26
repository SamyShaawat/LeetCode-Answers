class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        found = {}

        for index, value in enumerate(nums):
            if value in found and index - found[value] <= k:
                return True
            else:
                found[value] = index
        return False
      
            
