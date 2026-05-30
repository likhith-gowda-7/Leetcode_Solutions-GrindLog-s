# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sub_dfs(root,subroot):
            if(not root and not subroot):
                return True
            if((not root or not subroot) or root.val!=subroot.val):
                return False
            return sub_dfs(root.left,subroot.left) and sub_dfs(root.right,subroot.right)

        self.is_exists=False
        def dfs(root):
            if(self.is_exists):
                return
            if(not root):
                return
            if(not self.is_exists and root.val==subRoot.val):
                self.is_exists=sub_dfs(root,subRoot)
                
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return self.is_exists