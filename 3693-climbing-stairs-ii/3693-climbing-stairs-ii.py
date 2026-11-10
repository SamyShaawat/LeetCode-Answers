class Solution:
    def climbStairs(self, n, costs):
        a=b=10**18;c=0
        for x in costs:a,b,c=b,c,min(c+1,b+4,a+9)+x
        return c