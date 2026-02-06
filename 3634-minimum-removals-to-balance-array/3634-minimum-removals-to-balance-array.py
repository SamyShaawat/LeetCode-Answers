class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = n  

        left = 0
        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1
            res = min(res, n - (right - left + 1))

        return res