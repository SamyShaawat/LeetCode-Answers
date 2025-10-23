class Solution:
    def getMod10(self, n: int, i: int) -> int:
        fast5 = [
            [1,0,0,0,0],
            [1,1,0,0,0],
            [1,2,1,0,0],
            [1,3,3,1,0],
            [1,4,1,4,1]
        ]
        xunzhi = [
            [0,6,2,8,4],
            [5,1,7,3,9]
        ]

        mod2 = 1
        mod5 = 1

        a, b = n, i
        while a > 0 or b > 0:
            na = a & 1
            nb = b & 1
            if nb and not na:
                mod2 = 0
                break
            a >>= 1
            b >>= 1

        a, b = n, i
        while a > 0 or b > 0:
            na = a % 5
            nb = b % 5
            mod5 = (mod5 * fast5[na][nb]) % 5
            a //= 5
            b //= 5

        return xunzhi[mod2][mod5]

    def hasSameDigits(self, s: str) -> bool:
        n = len(s) - 1
        left = 0
        right = 0

        for i in range(n + 1):
            val = ord(s[i]) - 48
            if i <= n - 1:
                left = (left + self.getMod10(n - 1, i) * val) % 10
            if i >= 1:
                right = (right + self.getMod10(n - 1, i - 1) * val) % 10

        return left == right
