class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return str(num) == str(int(str(num)[::-1]))[::-1]
        