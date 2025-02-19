class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        s= "".join(char for char in s if char.isalnum())
        print(s)
        return s[::] == s[::-1]