# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        total_nodes=0
        def dfs(node):
            if(not node):
                return [0,0]
            left=dfs(node.left)
            right=dfs(node.right)
            curr_sum=left[0]+right[0]+node.val
            curr_nodes=left[1]+right[1]+1
            average=curr_sum//curr_nodes
            if(average==node.val):
                nonlocal total_nodes
                total_nodes+=1
            return [curr_sum,curr_nodes]
        dfs(root)
        return total_nodes