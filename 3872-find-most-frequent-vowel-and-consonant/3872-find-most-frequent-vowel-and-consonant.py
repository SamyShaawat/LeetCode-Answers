class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = 'auoie'
        h = Counter(s)
        v = 0
        c = 0
        for key, value in h.items():
            if key in vowels:
                v = max(v, value)
            elif key not in vowels:
                c = max(c, value)
        return v + c

            
        