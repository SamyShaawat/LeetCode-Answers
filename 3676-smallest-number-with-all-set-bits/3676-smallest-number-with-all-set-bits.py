class Solution:
    def smallestNumber(self, n: int) -> int:
        x= 1 
        while x < n : 
            print("shift: ",x << 1)
            print("shitt with or: ", (x << 1)|1)
            x = (x << 1) | 1 
        return x