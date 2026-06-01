# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.mini=float("inf")
        prev=None
        def dfs(root):
            nonlocal prev
            if(not root):
                return 0
            dfs(root.left)
            if(prev):
                self.mini=min(self.mini,abs(prev.val-root.val))
            prev=root
            dfs(root.right)
        dfs(root)
        return self.mini
