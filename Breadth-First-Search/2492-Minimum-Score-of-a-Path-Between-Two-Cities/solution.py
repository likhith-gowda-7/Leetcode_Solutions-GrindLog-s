class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent=list(range(n+1))
        min_score=[float('inf')]*(n+1)
        def find(x):
            if(parent[x]==x):
                return x
            parent[x]=find(parent[x])
            return parent[x]
        def union(x,y,cost):
            x_root=find(x)
            y_root=find(y)
            if(min_score[x_root]<min_score[y_root]):
                min_score[x_root]=min(min_score[x_root],cost)
                parent[y_root]=x_root
            else:
                min_score[y_root]=min(min_score[y_root],cost)
                parent[x_root]=y_root
        for node1,node2,cost in roads:
            union(node1,node2,cost)
        return min_score[find(n)]