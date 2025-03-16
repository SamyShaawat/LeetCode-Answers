class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, h = 1, ranks[0]*cars*cars
        res = 0
        def repaired_count(t):
            count = 0 
            for r in ranks:
                count+= int(sqrt(t/r))
            return count
        while l <= h:
            m = (l+h) // 2
            if repaired_count(m) >= cars:
                res = m
                h = m - 1
            else:
                l  = m + 1
        return res 
        