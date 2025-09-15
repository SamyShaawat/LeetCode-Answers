class Solution:
    def canBeTypedWords(self, s: str, t: str) -> int:
        return sum(not {*w}&{*t} for w in s.split())