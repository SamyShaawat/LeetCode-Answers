class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        S = Counter(s)
        T = Counter(t)
        for key in S:
            if S[key] in T.values():
                continue
            else:
                return False
        return True        