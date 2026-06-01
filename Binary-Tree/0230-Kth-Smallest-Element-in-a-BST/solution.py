# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c=0
        kth=None
        def inorder(root):
            if(not root):
                return None
            nonlocal c,kth
            inorder(root.left)
            c+=1
            if(k==c):
                kth=root.val
                return 
            inorder(root.right)
        inorder(root)
        return kth