class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        p = -2; a = b = best = 0
        for x in nums:
            if x == p:
                b = a + 1
                if b > best: best = b
                continue
            if x == p + 1:
                m, d = a, b
            elif x == p + 2:
                m, d = b, 0
            else:
                m = d = 0
            a = m + 1
            b = d + 1
            if b > best: best = b
            if a > best: best = a
            p = x
        return best
