class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        l, r = 1, max(candies)
        best = 0
        while l <= r:
            mid = (l + r) // 2
            childern_count = sum(pile//mid for pile in candies) # total children that can rec eive 'mid' candies
            print(childern_count)
            if childern_count >= k:
                best = mid 
                l = mid + 1 # try for a larger size
            else:
                r = mid - 1 # try a smaller size
        return best
        