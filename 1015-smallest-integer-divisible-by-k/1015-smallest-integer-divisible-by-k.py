class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        Find smallest repunit (number with only 1's) divisible by k
        :type k: int
        :rtype: int - length of smallest repunit, or -1 if none exists
        """
        n = 0  # Current remainder tracker
        
        # Try repunits of length 1 to k
        for i in range(1, k + 1):
            # Build next repunit using modular arithmetic
            n = (n * 10 + 1) % k
            
            # Check if current repunit is divisible by k
            if n == 0:
                return i
                
        # No solution exists
        return -1