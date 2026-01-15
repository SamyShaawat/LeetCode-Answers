class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def maxLen(Bars: List[int]):
            count,length = 2,2
            for i in range(1,len(Bars)):
                if Bars[i] - Bars[i-1] == 1: count += 1
                else: count = 2
                length = max(length, count)
            return length
        hBars.sort(), vBars.sort()
        side = min(maxLen(hBars), maxLen(vBars))
        return side * side