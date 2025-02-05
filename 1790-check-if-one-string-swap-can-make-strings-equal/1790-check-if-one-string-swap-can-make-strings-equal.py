class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        indexes = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indexes.append(i)
            if len(indexes) > 2:
                return False
        if len(indexes) == 2:
            i, j = indexes
            return s1[i] == s2[j] and s1[j] == s2[i]
        return len(indexes) == 0