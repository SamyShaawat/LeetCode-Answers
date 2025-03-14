class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)
        res = 0
        while l <= r:
            mid = (l+r) // 2
            childern_count = sum(pile//mid for pile in candies)
            print(childern_count)
            if childern_count >= k:
                res = mid 
                l = mid + 1
            else:
                r = mid - 1 
        return res
        