class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_value = 0
        for num in nums:
            max_or_value |= num
        return self._count_subsets(nums, 0, 0, max_or_value)

    def _count_subsets(
        self, nums: List[int], index: int, current_or: int, target_or: int
    ) -> int:
        # Base case: reached the end of the array
        if index == len(nums):
            return 1 if current_or == target_or else 0

        # Don't include the current number
        count_without = self._count_subsets(
            nums, index + 1, current_or, target_or
        )

        # Include the current number
        count_with = self._count_subsets(
            nums, index + 1, current_or | nums[index], target_or
        )

        # Return the sum of both cases
        return count_without + count_with