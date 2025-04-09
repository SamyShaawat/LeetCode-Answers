class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        c = 0

        for i in range(left, right + 1):
            if i.bit_count() in primes:
                c += 1
                
        return c