# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same=True
        def dfs(root1,root2):
            #early exits after the mismatch is found
            if(not self.same):
                return 
            #this the base case, if both the nodes are null then it mean it's the end of the tree
            if(not root1 and not root2):
                return
            #if only one of them are null or node value's are not equal then it mean's its a mismatch
            if((not root1 or not root2) or root1.val!=root2.val):
                self.same=False
            #this return ensures that we won't go or apply recursion to it's subtree after the mismatch is found
                return 
            
            dfs(root1.left,root2.left)
            dfs(root1.right,root2.right)
        dfs(p,q)
        return self.same
        