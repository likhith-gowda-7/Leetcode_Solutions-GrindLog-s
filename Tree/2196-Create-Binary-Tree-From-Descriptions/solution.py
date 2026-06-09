# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes=defaultdict(list)
        for node,child,side in descriptions:
            curr_node=node
            if(node in nodes):
                curr_node=nodes[node][1]
            else:
                curr_node=TreeNode(node)
                nodes[node]=[False,curr_node]
            children=child
            if(child in nodes):
                children=nodes[child][1]
                nodes[child][0]=True
            else:
                children=TreeNode(child)
                nodes[child]=[True,children]
            #connect them
            if(side):
                curr_node.left=children
            else:
                curr_node.right=children
        for key,val in nodes.items():
            if(val[0]==False):
                return val[1]
        

