# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder_dfs(root):
            if(not root):
                return
            nonlocal curr_val,count,maxi,res
            inorder_dfs(root.left)
            if(curr_val==root.val):
                count+=1
            else:
                count=1
            curr_val=root.val
            if(maxi==count):
                res.append(root.val)
            elif(count>maxi):
                maxi=count
                res=[root.val]
            inorder_dfs(root.right)
        #variable 
        curr_val=None
        count=0
        maxi=0
        res=[]
        inorder_dfs(root)
        return res

            