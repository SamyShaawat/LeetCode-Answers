# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res= []
        def traverse_dfs(node, path):
            if not (node.left or node.right):
                res.append("->".join(path))
            if node.left:
                traverse_dfs(node.left, path + [str(node.left.val)])
            if node.right:
                traverse_dfs(node.right, path + [str(node.right.val)])
        traverse_dfs(root, [str(root.val)])
        return res
        