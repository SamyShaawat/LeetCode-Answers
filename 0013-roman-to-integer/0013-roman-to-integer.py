class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap= {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M": 1000
        }
        res = 0 
        for i in range(len(s)):
            if i+1 < len(s) and hashmap[s[i]] < hashmap[s[i+1]]:
                res -= hashmap[s[i]] 
            else:
                res += hashmap[s[i]] 
        return res