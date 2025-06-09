class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countSteps(n, first, last):
            steps = 0
            while first <= n:
                steps += min(n + 1, last) - first
                first *= 10
                last *= 10
            return steps
        curr = 1
        k -= 1
        while k > 0:
            steps = countSteps(n, curr, curr + 1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
        return curr