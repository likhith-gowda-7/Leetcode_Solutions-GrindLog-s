"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_of_node={None:None}
        node=head
        while node:
            copy=Node(node.val)
            copy_of_node[node]=copy
            node=node.next
        node=head
        while node:
            copy=copy_of_node[node]
            copy.next=copy_of_node[node.next]
            copy.random=copy_of_node[node.random]
            node=node.next
        return copy_of_node[head]
