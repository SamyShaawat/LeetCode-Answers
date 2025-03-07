class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def get_primes(my_list):
            """Optimized prime checking using Sieve of Eratosthenes"""
            if not my_list:
                return []

            n = max(my_list)
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

            for i in range(2, int(sqrt(n)) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False

            # Extract primes from the given range
            return [x for x in my_list if is_prime[x]]

        original = range(left, right + 1)
        primes = get_primes(original)

        if len(primes) < 2:
            return [-1, -1]

        res = [-1, -1]
        diff = float("inf")

        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < diff:
                diff = primes[i] - primes[i - 1]
                res = [primes[i - 1], primes[i]]

        return res