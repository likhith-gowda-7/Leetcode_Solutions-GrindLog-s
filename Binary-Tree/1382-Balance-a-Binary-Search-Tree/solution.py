# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res=[]
        def dfs(node):
            if(not node):
                return None
            nonlocal res
            left=dfs(node.left)
            res.append(node.val)
            right=dfs(node.right)
        dfs(root)
        n=len(res)
        def bst(l,r):
            if(l>r):
                return None
            mid=(l+r)//2
            node=TreeNode(res[mid])
            node.left=bst(l,mid-1)
            node.right=bst(mid+1,r)
            return node
        return bst(0,n-1)