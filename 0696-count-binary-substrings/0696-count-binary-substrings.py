class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return sum(map(min,pairwise(map(len,findall(r'0+|1+',s)))))