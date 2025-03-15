class Solution:
    def numberOfCuts(self, n: int) -> int:
        if (n%2 and n > 1):
            return n
        else:
            return int(n/2)