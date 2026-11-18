class Solution:
    def minChanges(self, s: str) -> int:
        return sum(map(str.__ne__, s[::2], s[1::2]))
