# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev=None
        bst=True
        def inorder(root):
            nonlocal prev,bst
            if(not root or not bst):
                return
            inorder(root.left)
            if(prev!=None and prev>=root.val):
                bst=False
                return
            prev=root.val
            inorder(root.right)
        inorder(root)
        return bst 
            
                