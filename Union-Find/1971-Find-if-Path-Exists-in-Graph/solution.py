class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    #Union Find(Disjoint-set) Solution
        parent=list(range(n))
        def find(node):
            #this checks if we are in the root node or not
            if(parent[node]!=node):
                parent[node]=find(parent[node])
            return parent[node]
        for u,v in edges:
            u_root=find(u)
            v_root=find(v)
            parent[u_root]=parent[v_root]
        return find(source)==find(destination)