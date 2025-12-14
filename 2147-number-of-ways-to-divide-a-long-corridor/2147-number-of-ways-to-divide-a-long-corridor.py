class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7

        total_seats = corridor.count("S")
        if total_seats == 0 or total_seats % 2 == 1:
            return 0

        ans = 1
        seat = 0
        plant = 0

        for c in corridor:
            if c == "S":
                if seat == 2:
                    ans = ans * (plant + 1) % mod
                    plant = 0
                    seat = 0
                seat += 1
            else:  
                if seat == 2:
                    plant += 1

        return ans