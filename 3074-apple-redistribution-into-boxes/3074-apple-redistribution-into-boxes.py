class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        total = sum(apple)

        fq = [0] * 51
        high, low = 0, 51
        for c in capacity:
            fq[c] += 1
            high = max(high, c)
            low = min(low, c)

        res = 0
        for i in range(high, low - 1, -1):
            while fq[i] > 0 and total > 0:
                total -= i
                fq[i] -= 1
                res += 1

        return res
