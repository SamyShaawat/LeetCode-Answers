class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # In case k is greater than n
        rotated = [0] * n
        for i in range(n):
            # Place each element in its new position
            rotated[(i + k) % n] = nums[i]
        # Copy the rotated array back to nums
        nums[:] = rotated
        
        