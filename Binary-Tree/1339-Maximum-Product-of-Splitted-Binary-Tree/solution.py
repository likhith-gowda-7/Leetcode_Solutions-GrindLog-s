# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self,node):
        def dfs(node):
            if(not node):
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            return node.val+left+right
        return dfs(node)
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod=pow(10,9)+7
        total=self.find(root)
        max_prod=0
        def dfs(node):
            if(not node):
                return 0
            nonlocal max_prod
            left=dfs(node.left)
            right=dfs(node.right)
            take_left=(total-left)*left
            take_right=(total-right)*right
            max_prod=max(max_prod,max(take_left,take_right))
            return node.val+left+right
        dfs(root)
        return max_prod%mod