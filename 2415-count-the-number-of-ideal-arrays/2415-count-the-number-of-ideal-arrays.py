class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9+7

        # sieve
        sieve = list(range(maxValue+1))
        for i in range(2, int(maxValue**0.5)+1):
            if sieve[i] == i: # we have not touched it yet
                for j in range(i*i, maxValue+1, i): # +i until we cant
                    if sieve[j] == j: # untouched
                        sieve[j] = i
        
        # get all prime factors of n
        def factors(n):
            res = defaultdict(int)
            while n > 1:
                smallest_prime = sieve[n]
                res[smallest_prime] += 1
                n //= smallest_prime
            return res
        
        res = 0
        for i in range(1, maxValue+1):
            ways = 1
            for exp in factors(i).values():
                # stars and bars ncr
                ways = (ways * math.comb(n - 1 + exp, exp)) % MOD
            res += ways % MOD
        return res % MOD
