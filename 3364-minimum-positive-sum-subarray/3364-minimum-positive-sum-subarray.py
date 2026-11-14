class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        p = [0]
        a = 0
        for x in nums:
            a += x
            p.append(a)
        best = 1000000000
        for i in range(l, len(p)):
            pi = p[i]
            for q in p[i - r if i > r else 0:i - l + 1]:
                s = pi - q
                if 0 < s < best:
                    best = s
        return -1 if best == 1000000000 else best
