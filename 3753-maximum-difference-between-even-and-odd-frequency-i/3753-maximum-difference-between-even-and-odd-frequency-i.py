class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = Counter(s)
        # print("HashMap:", hashmap)

        odd_freqs = [v for v in hashmap.values() if v % 2 == 1]
        even_freqs = [v for v in hashmap.values() if v % 2 == 0]

        max_diff = float('-inf')

        for odd in odd_freqs:
            for even in even_freqs:
                diff = odd - even
                max_diff = max(max_diff, diff)
                
        if max_diff == float('-inf'):
            return 0

        return max_diff
