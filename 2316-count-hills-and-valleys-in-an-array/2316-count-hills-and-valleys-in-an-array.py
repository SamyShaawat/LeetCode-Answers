class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        l, m, r = 0, 1, 2
        res = 0

        while r < n:
            while m < n and nums[l] == nums[m]:
                m += 1

            r = m + 1
            while r < n and nums[m] == nums[r]:
                r += 1

            if r < n and ((nums[l] > nums[m] and nums[r] > nums[m]) or
                          (nums[l] < nums[m] and nums[r] < nums[m])):
                res += 1

            l, m = m, r

        return res
