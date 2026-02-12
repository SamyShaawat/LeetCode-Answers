class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        m = float('-inf')
        for i in range(n):
            freq = {}
            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1

                values = freq.values()
                if len(set(values)) == 1:
                    m = max(m, j - i + 1)
                    
        return m