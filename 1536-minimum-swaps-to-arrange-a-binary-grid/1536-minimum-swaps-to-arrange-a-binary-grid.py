class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        
        # Count trailing zeros
        trailing = []
        for row in grid:
            count = 0
            for num in reversed(row):
                if num == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0
        
        for i in range(n):
            required = n - 1 - i
            j = i
            
            # Find suitable row
            while j < n and trailing[j] < required:
                j += 1
            
            if j == n:
                return -1
            
            # Move row up step-by-step
            while j > i:
                trailing[j], trailing[j-1] = trailing[j-1], trailing[j]
                swaps += 1
                j -= 1
        
        return swaps