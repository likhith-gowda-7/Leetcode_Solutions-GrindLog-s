# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if(depth-1==0):
            node=TreeNode(val)
            node.left=root
            return node
        q=deque([(root,1)])
        check=depth-1
        while q:
            if(q[0][1]==check):
                break
            node,level=q.popleft()
            if(node.left):
                q.append((node.left,level+1))
            if(node.right):
                q.append((node.right,level+1))
        while q:
            node,level=q.popleft()
            dummy_node1=TreeNode(val)
            dummy_node2=TreeNode(val)
            dummy_node1.left=node.left
            dummy_node2.right=node.right
            node.left=dummy_node1
            node.right=dummy_node2
        return root