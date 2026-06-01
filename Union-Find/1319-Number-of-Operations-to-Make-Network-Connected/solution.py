class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if(len(connections)<(n-1)):
            return -1
        #Solution using Union-Find
        parent=list(range(n))
        size=[1]*n
        #this hold extra cables
        extra_edges=0
        def find(x):
            if(parent[x]!=x):
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            x_root=find(x)
            y_root=find(y)
            if(x_root==y_root):
                nonlocal extra_edges
                extra_edges+=1
                return False
            else:
                if(size[x_root]<size[y_root]):
                    parent[x_root]=y_root
                    size[y_root]+=size[x_root]
                else:
                    parent[y_root]=x_root
                    size[x_root]+=size[y_root]
                return True
        connected=1
        for node1,node2 in connections:
            if(union(node1,node2)):
                connected+=1
        remaining=n-connected
        res=remaining-extra_edges
        return remaining
        

        