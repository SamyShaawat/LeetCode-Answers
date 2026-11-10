class Solution:
    def climbStairs(self, n, costs):
        a=b=10**18;c=0
        for x in costs:d=c+1;e=b+4;f=a+9;a=b;b=c;c=(d if d<e else e)+x if d<f else (f if f<e else e)+x
        return c