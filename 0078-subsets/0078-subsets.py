class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sol, res = [], []
        def backtrack(i):
            if i == n: # Base case: if we have considered all elements
                res.append(sol[:])  # Add a copy of the current subset to res
                return
            # Exclude the current element and move to the next
            backtrack(i+1)

            # Include the current element and move to the next
            sol.append(nums[i])
            backtrack(i+1)

            # Backtrack by removing the last added element
            sol.pop()
        backtrack(0)
        return res 
        