class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()  # Sort the numbers in-place.
        missing_pos = 1  # Initialize the first missing positive number to 1.
        for num in nums:
            if num == missing_pos:
                missing_pos += 1  # Found the current smallest missing positive, check for the next one.
            elif num > missing_pos:
                break  # No need to proceed further as we found the missing number.
        return missing_pos        