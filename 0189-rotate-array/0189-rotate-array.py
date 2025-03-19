class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # In case k is greater than n
        for _ in range(k):
            # Rotate array by one step
            last = nums[-1]
            for i in range(n-1, 0, -1):
                nums[i] = nums[i-1]
            nums[0] = last
        
        