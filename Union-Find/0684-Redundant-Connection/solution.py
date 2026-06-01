class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=list(range(n+1))
        rank=[1]*(n+1)
        def find(x):
            if(parent[x]!=x):
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            x_root=find(x)
            y_root=find(y)
            #for cycle detection, if any edge forms a cycle return that edge
            if(x_root==y_root):
                return False
            else:
                if(rank[x_root]<rank[y_root]):
                    parent[x_root]=y_root
                    #updating the rank for that root after merging
                    rank[y_root]+=rank[x_root]
                else:
                    parent[y_root]=x_root
                    rank[x_root]+=rank[y_root]
                return True
        for x,y in edges:
            if(not union(x,y)):
                return [x,y]
        