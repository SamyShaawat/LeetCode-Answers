class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a,b,c = nums
        if (a + b > c) and (a + c > b) and (b + c > a):
            if (a == b) and (b == c):
                return "equilateral"
            elif (a == b) or (b == c) or (a==c):
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"



        