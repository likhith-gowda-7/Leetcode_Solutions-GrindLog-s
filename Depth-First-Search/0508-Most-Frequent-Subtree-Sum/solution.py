# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        h1={}
        res=[]
        maxi=0
        def dfs(root):
            if(not root):
                return 0
            nonlocal h1,res,maxi
            left=dfs(root.left)
            right=dfs(root.right)
            nodes_sum=left+right+root.val
            h1[nodes_sum]=h1.get(nodes_sum,0)+1
            count=h1[nodes_sum]
            if(count==maxi):
                res.append(nodes_sum)
            elif(count>maxi):
                maxi=count
                res=[nodes_sum]
            return nodes_sum
        dfs(root)
        return res