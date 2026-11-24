class Solution:
    def maxLength(self, nums: List[int]) -> int:
        m = (0, 0, 1, 2, 1, 4, 3, 8, 1, 2, 5)  # prime bitmask of 0..10
        best = 2
        l = cur = 0
        r = 0
        for x in nums:
            b = m[x]
            while cur & b:
                cur ^= m[nums[l]]
                l += 1
            cur |= b
            r += 1
            if r - l > best:
                best = r - l
        return best
