class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def normalize(N):
            ans = 0
            less = False  # whether the converted number is less than N
            for n in map(int, str(N)):
                if less:
                    ans = ans * 10 + limit
                elif n > limit:
                    less = True
                    ans = ans * 10 + limit
                else:
                    ans = ans * 10 + n
            return ans

        def count(N):
            ans = 0
            base = limit + 1
            prefix = str(N)[:-len(s)]
            for n in prefix:
                ans = ans * base + int(n)
            if int(prefix + s) <= N:
                ans += 1
            return ans

        return count(normalize(finish)) - count(normalize(start-1))