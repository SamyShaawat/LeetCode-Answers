class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        mystring = ""
        for digit in digits:
            mystring += str(digit)
        addOne = str(int(mystring)+1)
        res = [int(n) for n in addOne]
        return res
        