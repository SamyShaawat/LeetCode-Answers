class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: list[list[int]]) -> int:
        
        n += 1
        conflictingPairs.sort(key=lambda p: max(*p))
        conflictingPairs.append([n, n])
        maxDiff, maxLeft, remain = 0, 0, 0
        maxAlterLeft, altRemain = 0, 0
        for left, right in conflictingPairs:
            if left > right:
                left, right = right, left
            if left > maxLeft:
                maxDiff = max(maxDiff, (maxAlterLeft - maxLeft) * (n - right) + remain - altRemain)
                altRemain = remain
                maxAlterLeft = maxLeft
                remain += (left - maxLeft) * (n - right)
                maxLeft = left
            elif left > maxAlterLeft:
                altRemain += (left - maxAlterLeft) * (n - right)
                maxAlterLeft = left
        return (n - 1) * n // 2 - remain + maxDiff