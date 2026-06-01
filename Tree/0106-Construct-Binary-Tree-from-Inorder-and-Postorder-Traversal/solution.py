# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos=len(postorder)-1
        h1={}
        for i in range(len(inorder)):
            h1[inorder[i]]=i
        def dfs(left,right):
            if(left>right):
                return
            nonlocal pos,h1
            root=TreeNode(postorder[pos])
            mid=h1[postorder[pos]]
            pos-=1
            root.right=dfs(mid+1,right)
            root.left=dfs(left,mid-1)
            return root
        return dfs(0,len(inorder)-1)