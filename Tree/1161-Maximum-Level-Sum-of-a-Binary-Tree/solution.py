# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque()
        if(root):
            q.append((root,1))
        level_sum=defaultdict(int)
        while q:
            node,level=q.popleft()
            level_sum[level]+=node.val
            if(node.left):
                q.append((node.left,level+1))
            if(node.right):
                q.append((node.right,level+1))
        maxi=float('-inf')
        max_level=0
        for key,val in level_sum.items():
            if(val>maxi):
                maxi=val
                max_level=key
        return max_level

        