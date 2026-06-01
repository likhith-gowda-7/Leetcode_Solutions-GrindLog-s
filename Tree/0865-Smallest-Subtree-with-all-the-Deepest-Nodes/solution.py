# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self,root):
        if(not root):
            return 0
        level=0
        q=deque([root])
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if(node.right):
                    q.append(node.right)
                if(node.left):
                    q.append(node.left)
            level+=1
        return level

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        maxi=self.find(root)
        def dfs(node,level):
            if(not node):
                return None
            if(level==maxi):
                return node
            left=dfs(node.left,level+1)
            right=dfs(node.right,level+1)
            if(left and right):
                return node
            return left if(left) else right
        return dfs(root,1)