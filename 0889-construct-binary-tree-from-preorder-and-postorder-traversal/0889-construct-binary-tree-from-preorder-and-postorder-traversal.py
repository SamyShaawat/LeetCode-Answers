# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # preorder = root, left, right
        # postorder = left, right, root

        def makeTree():
            print("makeTree called:")
            print("Preorder:", preorder)
            print("Postorder:", postorder)
            
            node_val = postorder.pop()
            node = TreeNode(node_val)
            print("Created node with value:", node_val)

            if preorder and node.val != preorder[-1]:
                print("node.val:", node.val, "!= preorder[-1]:", preorder[-1], "-> Construct right subtree")
                node.right = makeTree()
            else:
                print("Skipping right subtree for node", node.val)

            if preorder and node.val != preorder[-1]:
                print("node.val:", node.val, "!= preorder[-1]:", preorder[-1], "-> Construct left subtree")
                node.left = makeTree()
            else:
                print("Skipping left subtree for node", node.val)

            if preorder:
                popped = preorder.pop()
                print("Popped", popped, "from preorder (used as root for node", node.val, ")")
            
            print("Returning node", node.val)
            return node

        return makeTree()

