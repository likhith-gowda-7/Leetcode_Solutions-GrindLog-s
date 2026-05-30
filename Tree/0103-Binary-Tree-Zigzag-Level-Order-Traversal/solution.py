# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        if(root):
            q.append(root)
        rev=0
        res=[]
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            if(rev):
                res.append(level[::-1])
            else:
                res.append(level)
            rev^=1
        return res




