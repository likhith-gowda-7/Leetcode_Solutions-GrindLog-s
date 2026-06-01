# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if(not root):
            return root
        if(root.val<key):
            root.right=self.deleteNode(root.right,key)
        elif(root.val>key):
            root.left=self.deleteNode(root.left,key)
        else:
            if(not root.right):
                return root.left
            elif(not root.left):
                return root.right
            curr=root.right
            while curr.left:
                curr=curr.left
            #Making the minimium as the new value for the deleted node
            root.val=curr.val
            #Then deleting that min value we just found and finding a new value for it
            root.right=self.deleteNode(root.right,curr.val)
        return root
    
        