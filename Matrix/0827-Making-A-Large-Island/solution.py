class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        parent=list(range(n*n))
        size=[1]*(n*n)
        root_to_size={}
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
        def check(row,col):
            if(row<0 or row>=n or col<0 or col>=n or grid[row][col]==0):
                return False
            return True
        zeros=[]
        for row in range(n):
            for col in range(n):
                if(grid[row][col]!=0):
                    node1=(row*n)+col
                    for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
                        ro=row+r
                        co=col+c
                        if(check(ro,co)):
                            node2=(ro*n)+co
                            union(node1,node2)
                    root_to_size[find(node1)]=size[find(node1)]
                else:
                    zeros.append((row,col))
        largest_island=max(size)
        while zeros:
            row,col=zeros.pop()
            unique_roots=set()
            curr_size=1
            for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
                ro=row+r
                co=col+c
                if(check(ro,co)):
                    node2=find((ro*n)+co)
                    if(node2 not in unique_roots):
                        curr_size+=root_to_size[node2]
                        unique_roots.add(node2)
            largest_island=max(largest_island,curr_size)
        return largest_island