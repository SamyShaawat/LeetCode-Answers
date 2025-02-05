class Solution:
    def isPalindrome(self, x: int) -> bool:
        stg = str(x)
        return stg[::] == stg[::-1]