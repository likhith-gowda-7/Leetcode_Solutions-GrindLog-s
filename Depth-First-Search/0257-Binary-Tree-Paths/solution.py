# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        def dfs(root,s):
            nonlocal res
            if(not root):
                return None
            s+="#"+str(root.val)
            left=dfs(root.left,s)
            right=dfs(root.right,s)
            if(not left and not right):
                data=s.split('#')[1:]
                val="->".join(data)
                res.append(val)
            return root
        dfs(root,"")
        return res