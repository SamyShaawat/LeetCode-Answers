class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(str(num))

        num1, num2 = "", ""

        for i, digit in enumerate(digits):
            if i % 2 == 0:
                num1 += digit
            else:
                num2 += digit
        return int(num1) + int(num2)
        