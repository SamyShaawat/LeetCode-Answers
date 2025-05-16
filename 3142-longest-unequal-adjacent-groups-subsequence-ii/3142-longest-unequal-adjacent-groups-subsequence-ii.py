class Solution:
    def getWordsInLongestSubsequence(self, words, groups):
        from functools import lru_cache

        def hamming_dist(w1, w2):
            return sum(a != b for a, b in zip(w1, w2)) == 1

        n = len(words)
        @lru_cache(None)
        def dfs(i, last_group, last_word):
            if i == n:
                return []
            take = []
            if len(words[i]) == len(last_word) and hamming_dist(last_word, words[i]) and groups[i] != last_group:
                take = [words[i]] + dfs(i + 1, groups[i], words[i])
            skip = dfs(i + 1, last_group, last_word)
            return take if len(take) > len(skip) else skip

        res = []
        for i in range(n):
            curr = [words[i]] + dfs(i + 1, groups[i], words[i])
            if len(curr) > len(res):
                res = curr
        return res