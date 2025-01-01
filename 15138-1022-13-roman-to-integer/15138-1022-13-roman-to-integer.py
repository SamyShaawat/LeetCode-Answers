class Solution:
    def romanToInt(self, s: str) -> int:
        dict1= {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M": 1000
        }
        lst = [dict1.get(char,0) for char in s]
        result = 0
        for i in range(len(lst)-1):
            if lst[i] < lst[i+1]:
                result -= lst[i]
            else:
                result += lst[i]
        
        result += lst[-1]
        return result
