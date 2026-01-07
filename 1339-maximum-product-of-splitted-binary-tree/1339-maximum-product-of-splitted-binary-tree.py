class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sums = []
        maxi = 0

        def dfs(node):
            if not node:
                return 0
            curr_sum = node.val+dfs(node.left)+dfs(node.right)
            all_sums.append(curr_sum)
            return curr_sum
        
        total = dfs(root)

        for x in all_sums:
            maxi = max(maxi, (total-x)*x)
        
        return maxi%(10**9 + 7)