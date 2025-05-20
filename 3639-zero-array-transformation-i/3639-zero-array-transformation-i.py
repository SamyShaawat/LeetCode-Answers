class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff_array = [0] * (n+1) 

        # Apply the difference array technique
        for start, end in queries:
            diff_array[start] += 1
            if end + 1 < n:
                diff_array[end + 1] -= 1

        current = 0
        for index in range(n):
            current += diff_array[index]
            if nums[index] > current:
                return False

        return True
