class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        all_nums = [num for row in grid for num in row]
        mod = all_nums[0] % x

        if any(num % x != mod for num in all_nums):
            return -1

        all_nums.sort()
        median = all_nums[len(all_nums) // 2]
        return sum(abs(num - median) // x for num in all_nums)