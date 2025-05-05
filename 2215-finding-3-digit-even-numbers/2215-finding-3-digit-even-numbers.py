class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res, cnt = [], Counter(digits)
        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 10, 2):
                    if cnt[i] > 0 and cnt[j] > (i == j) and cnt[k] > (k == i) + (k == j):
                        res.append(i * 100 + j * 10 + k)
        return res