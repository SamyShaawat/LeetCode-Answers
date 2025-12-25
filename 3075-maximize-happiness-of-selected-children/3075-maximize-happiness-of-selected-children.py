class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        res = 0
        count = 0
        for i in range(len(happiness) - 1, len(happiness) - k - 1, -1):
            if happiness[i] - count > 0:
                res += (happiness[i] - count)
            count += 1
        return res