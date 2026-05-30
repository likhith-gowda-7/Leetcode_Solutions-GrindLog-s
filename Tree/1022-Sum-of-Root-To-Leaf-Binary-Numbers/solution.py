# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def dfs(node,number):
            if(not node.left and not node.right):
                self.res+=number
                return None
            if(node.left):
                val=number<<1|node.left.val
                dfs(node.left,val)
            if(node.right):
                val=number<<1|node.right.val
                dfs(node.right,val)
        dfs(root,root.val)
        return self.res