class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj_list=defaultdict(list)
        for u,v,cost in edges:
            adj_list[u].append((v,cost))
            adj_list[v].append((u,cost*2))
        heap=[(0,0)]
        distance=[float('inf')]*n
        distance[0]=0
        while heap:
            curr_cost,node=heappop(heap)
            if(node==n-1):
                return distance[n-1]
            for v,cost in adj_list[node]:
                dist=curr_cost+cost
                if(dist<distance[v]):
                    heappush(heap,(dist,v))
                    distance[v]=dist
        return -1   
