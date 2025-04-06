class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()  # Sort the numbers to ensure that for any nums[i] > nums[j], nums[i] % nums[j] can be checked properly
        n = len(nums)

        groupSize = [1] * n  # Initialize the size of the largest divisible subset ending at each index
        prevElement = [-1] * n  # Keep track of previous index in the subset chain
        maxIndex = 0  # Index of the last element in the largest divisible subset found so far

        # Dynamic Programming to find the size of the largest divisible subset ending at each number
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:  # Check if nums[i] can be appended to the subset ending with nums[j]
                    if groupSize[i] < 1 + groupSize[j]:  # Update group size if a longer subset is found
                        groupSize[i] = 1 + groupSize[j]
                        prevElement[i] = j  # Store the index of previous number in the chain
            # Update the index of the largest subset found so far
            if groupSize[i] > groupSize[maxIndex]:
                maxIndex = i

        # Reconstruct the subset by backtracking through prevElement
        result = []
        while maxIndex != -1:
            result.insert(0, nums[maxIndex])  # Insert at the beginning to maintain order
            maxIndex = prevElement[maxIndex]  # Move to the previous element in the subset chain

        return result  # Return the largest divisible subset
