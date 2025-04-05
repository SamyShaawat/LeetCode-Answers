class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isgood(i,j):
            return words[j].startswith(words[i]) and words[j].endswith(words[i])  
        n = len(words)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if isgood(i,j):
                    count += 1
        return count