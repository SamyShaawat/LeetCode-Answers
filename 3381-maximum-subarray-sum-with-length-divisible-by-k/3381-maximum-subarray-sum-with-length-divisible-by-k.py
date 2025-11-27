class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefSum = 0
        subMax = -sys.maxsize
        minSoFar = [sys.maxsize] * k
        minSoFar[(k - 1) % k] = 0

        for i, v in enumerate(nums):
            prefSum += v
            subMax = max(subMax, prefSum - minSoFar[i % k])
            minSoFar[i % k] = min(minSoFar[i % k], prefSum)

        return subMax
