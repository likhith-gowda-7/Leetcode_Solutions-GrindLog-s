# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        h1={}
        for i in range(len(inorder)):
            h1[inorder[i]]=i
        idx=0
        def dfs(left,right):
            if(left>right):
                return
            nonlocal h1,preorder,inorder,idx
            root=TreeNode(preorder[idx])
            mid=h1[preorder[idx]]
            idx+=1
            root.left=dfs(left,mid-1)
            root.right=dfs(mid+1,right)
            return root
        return dfs(0,len(inorder)-1)

        