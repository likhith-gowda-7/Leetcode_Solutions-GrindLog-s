# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack=[]
        if(root):
            stack.append(root)
        while stack:
            check=stack.pop()
            if(check.left):
                stack.append(check.left)
            if(check.right):
                stack.append(check.right)
            temp=check.left
            check.left=check.right
            check.right=temp
        return root