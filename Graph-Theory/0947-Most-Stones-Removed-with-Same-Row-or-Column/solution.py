class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row_max=max(stones)[0]
        col_max=max(stones,key=lambda x:x[1])[1]
        n=(row_max+col_max)+1
        parent=list(range(n+1))
        size=[1]*(n+1)
        def find(x):
            if(parent[x]!=x):
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            x_root=find(x)
            y_root=find(y)
            if(x_root==y_root):
                return
            else:
                if(size[x_root]<size[y_root]):
                    parent[x_root]=y_root
                    size[y_root]+=size[x_root]
                else:
                    parent[y_root]=x_root
                    size[x_root]+=size[y_root]
        used_nodes=set()
        for row,col in stones:
            #We do coordinate matching, meaning we consider the row and column as two different nodes
            node1=row
            node2=(col+row_max)+1
            union(node1,node2)
            used_nodes.add(node1)
            used_nodes.add(node2)
        roots=set(find(node) for node in used_nodes)
        return len(stones)-len(roots)
        
        
        