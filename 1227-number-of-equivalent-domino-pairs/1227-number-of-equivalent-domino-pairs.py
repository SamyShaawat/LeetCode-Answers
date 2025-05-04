class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        freq = defaultdict(int)

        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            count += freq[key]
            freq[key] += 1

        return count