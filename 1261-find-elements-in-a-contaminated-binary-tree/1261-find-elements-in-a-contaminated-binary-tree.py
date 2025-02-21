# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        def recover(node,val):
            if not node:
                return 
            self.values.add(val)
            if node.left:
                recover(node.left,2*val+1)
            if node.right:
                recover(node.right,2*val+2)

        recover(root,0)
        

    def find(self, target: int) -> bool:
        return target in self.values
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)