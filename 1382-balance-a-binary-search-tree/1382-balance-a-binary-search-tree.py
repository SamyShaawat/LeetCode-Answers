# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr=[]
        def inOrder( root):
            if not root: return
            inOrder(root.left)
            arr.append(root)
            inOrder(root.right)

        def balanceBST(l, r):
            if l>r: return None
            m=(l+r)>>1
            L=balanceBST(l, m-1)
            R=balanceBST(m+1, r)
            arr[m].left=L
            arr[m].right=R
            return arr[m]

        inOrder(root)
        return balanceBST(0, len(arr)-1)
        