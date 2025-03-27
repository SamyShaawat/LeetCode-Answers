class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sol, res = [], []
        def backtrack():
            if len(sol) == n:
                # res.append(sol.copy())
                # res.append(list(sol))
                res.append(sol[:])  # Add a copy of sol to res
                return
            for num in nums: # Iterate through each number in the input list
                if num not in sol: # Ensure unique elements in the current permutation
                    sol.append(num) # Choose the number
                    backtrack() # Recurse to build the next level
                    sol.pop() # Backtrack by removing the last added number

        backtrack()
        return res  # Return all generated permutations
