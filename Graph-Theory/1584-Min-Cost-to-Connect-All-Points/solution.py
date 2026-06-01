class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Prim's Algo
        n=len(points)
        MST_sum=0
        visited=[0]*n
        heap=[(0,0)]
        total_edges=0
        while total_edges<n:
            cost,node=heappop(heap)
            if(visited[node]):
                continue
            MST_sum+=cost
            visited[node]=1
            total_edges+=1    
            x1,y1=points[node]
            for neighbour,val in enumerate(points):
                if(not visited[neighbour]):
                    x2,y2=val
                    weight=abs(x1-x2)+abs(y1-y2)
                    heappush(heap,(weight,neighbour))
        return MST_sum    