class Solution:
    def findValidPair(self, s: str) -> str:
        cnt = collections.Counter(s)
        for i, c in enumerate(s):
            if i == 0: continue
            if s[i] != s[i - 1] and cnt[s[i]] == int(s[i]) and cnt[s[i - 1]] == int(s[i - 1]):
                return s[i - 1: i + 1] 
        return ""