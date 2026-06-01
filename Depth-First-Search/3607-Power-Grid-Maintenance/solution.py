class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent=list(range(c+1))
        def find(x):
            if(parent[x]!=x):
                parent[x]=find(parent[x])
            return parent[x]
        size=[1]*(c+1)
        def union(x,y):
            x_root=find(x)
            y_root=find(y)
            if(x_root==y_root):
                return
            if(size[x_root]<size[y_root]):
                parent[x_root]=y_root
                size[y_root] += 1
            else:
                parent[y_root]=x_root
                size[x_root] += 1

        for u,v in connections:
            union(u,v)
        branches=defaultdict(list)
        for i in range(1,c+1):
            root=find(i)
            heappush(branches[root],i)
        res=[]
        online=set(range(1,c+1))
        for mode,station in queries:
            if(mode==1):
                found=station
                if(station not in online):
                    root_station=find(station)
                    found=-1
                    while branches[root_station] and branches[root_station][0] not in online:
                        heappop(branches[root_station])
                    if(branches[root_station]):
                        found=branches[root_station][0]
                res.append(found)
            elif(station in online):
                online.remove(station)
        return res
