class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)
        i, j = 0, 0

        while i < S and j < T:
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
        return i == S
        
        