# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        nodes=[]
        q=deque([(root,1)])
        while q:
            node,node_level=q.popleft()
            nodes.append([node.val,node_level])
            if(node.left):
                q.append([node.left,node_level+1])
            if(node.right):
                q.append([node.right,node_level+1])
        height=nodes[-1][1]
        res=[[] for _ in range(height)]
        for node,level in nodes:
            #array indexing
            res[level-1].append(node)
        return res




