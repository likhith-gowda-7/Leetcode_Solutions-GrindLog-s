# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(not root):
            return []
        length=1
        q=deque([root])
        res=[]
        while q:
            curr_length=length
            while q and curr_length>1:
                curr=q.popleft()
                length-=1
                if(curr.left):
                    q.append(curr.left)
                    length+=1
                if(curr.right):
                    q.append(curr.right)
                    length+=1
                curr_length-=1
            node=q.popleft()
            length-=1
            res.append(node.val)
            if(node.left):
                q.append(node.left)
                length+=1
            if(node.right):
                q.append(node.right)
                length+=1
        return res

            