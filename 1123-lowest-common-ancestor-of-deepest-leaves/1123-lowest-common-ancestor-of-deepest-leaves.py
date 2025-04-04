# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None 
        self.caniadate = None
        self.max_depth = -1
        self.dfs(root,0)
        return self.caniadate
    def dfs(self,node, depth):
        if not node:
            return -1
        if not node.left and not node.right:
            if depth > self.max_depth:
                 self.caniadate = node
                 self.max_depth = depth 
            return depth
        l_depth = self.dfs(node.left, depth+1)
        r_depth = self.dfs(node.right, depth+1)

        if l_depth == r_depth == self.max_depth :
             self.caniadate = node
        return max(l_depth, r_depth)


        