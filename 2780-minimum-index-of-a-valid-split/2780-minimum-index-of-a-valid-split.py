class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        mp1 = Counter(nums)
        mp2 = Counter()

        for i, num in enumerate(nums):
            mp1[num] -= 1
            mp2[num] += 1
            if mp1[num] * 2 > len(nums) - i - 1 and mp2[num] * 2 > i + 1:
                return i
        return -1

        