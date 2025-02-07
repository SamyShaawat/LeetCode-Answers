class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # first solution Brute force one:
        n = len(pref)
        result = 0
        for word in words:
            if word[:n] == pref:
                result += 1
        return result 
        