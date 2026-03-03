class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        flip = False  # whether we have inverted odd number of times
        
        while n > 1:
            mid = 1 << (n - 1)       # 2^(n-1)
            length = (1 << n) - 1    # 2^n - 1
            
            if k == mid:
                # middle is always '1', but may be flipped
                return '0' if flip else '1'
            
            if k > mid:
                # mirror position and toggle flip
                k = length - k + 1
                flip = not flip
            
            # move to S(n-1)
            n -= 1
        
        # base case: S1 = "0"
        return '1' if flip else '0'