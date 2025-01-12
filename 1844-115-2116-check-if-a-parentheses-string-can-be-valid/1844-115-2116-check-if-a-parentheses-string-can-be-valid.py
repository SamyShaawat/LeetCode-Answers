class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        opened = 0
        for i in range(len(s)):
            if locked[i] == '0'or s[i] == '(':
                opened+=1
            else: 
                opened-=1
            if opened < 0:
                return False
        closed = 0
        for i in range(len(s)-1,-1,-1):
            if locked[i] == '0' or s[i] == ")":
                closed+=1
            else:
                closed-=1
            if closed < 0:
                return False
        return True