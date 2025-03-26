class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                if s[l+1:r+1] == s[l+1:r+1][::-1]:
                    return True
                if s[l:r+1-1] == s[l:r+1-1][::-1]:
                    return True 
                return False
            l, r = l+1, r -1
        return True