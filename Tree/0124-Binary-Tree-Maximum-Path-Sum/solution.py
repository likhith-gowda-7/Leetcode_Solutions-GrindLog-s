# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float("-inf")
        def dfs(root):
            if(not root):
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            curr=max(root.val,root.val+left,root.val+right,left+right+root.val)
            self.maxi=max(self.maxi,curr)
            return max(root.val,root.val+max(left,right))
        dfs(root)
        return self.maxi

            