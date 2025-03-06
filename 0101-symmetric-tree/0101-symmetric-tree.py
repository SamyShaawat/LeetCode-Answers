# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    def isMirror(self, leftTree: Optional[TreeNode], rightTree: Optional[TreeNode]) -> bool:
        if not leftTree and not rightTree:
            return True
        if not leftTree or not rightTree:
            return False
        return (leftTree.val == rightTree.val) and (self.isMirror(leftTree.left, rightTree.right)) and (self.isMirror(leftTree.right, rightTree.left))      
        