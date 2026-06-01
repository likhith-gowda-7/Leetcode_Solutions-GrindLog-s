"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if(not node):
            return None
        #we'll map node's address to it's deep copy address
        #Orginal address -> It's DeepCopy Address
        clone_map={}
        #the node , the node it belongs to(neighbour)
        clone_map[node]=Node(node.val)
        stack=[node]
        while stack:
            v=stack.pop()
            for n in v.neighbors:
                if(n not in clone_map):
                    new_node=Node(n.val)
                    clone_map[n]=new_node
                    stack.append(n)
                clone_map[v].neighbors.append(clone_map[n])
        return clone_map[node]
