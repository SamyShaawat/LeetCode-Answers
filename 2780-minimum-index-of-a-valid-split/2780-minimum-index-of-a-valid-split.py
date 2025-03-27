class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        mp1 = Counter(nums)  # Count occurrences of each number in the entire list
        mp2 = Counter()  # Counter to track occurrences in the left partition

        for i, num in enumerate(nums):  # Iterate over the list with index
            mp1[num] -= 1  # Decrease count in the right partition
            mp2[num] += 1  # Increase count in the left partition
            
            # Check if 'num' is dominant in both partitions
            if mp1[num] * 2 > len(nums) - i - 1 and mp2[num] * 2 > i + 1:
                return i  # Return the index where the split is valid
        
        return -1  # If no valid index is found, return -1
