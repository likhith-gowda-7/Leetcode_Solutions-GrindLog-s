class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list=defaultdict(list)
        for u,v,cost in flights:
            adj_list[u].append((v,cost))
        q=deque([(0,src,0)])
        costs=[1e9]*n
        costs[src]=0
        while q:
            stops,node,cost=q.popleft()
            for v,c in adj_list[node]:
                curr_cost=cost+c
                if((v==dst or (stops+1)<=k) and curr_cost<costs[v]):
                    costs[v]=curr_cost
                    q.append((stops+1,v,curr_cost))
        return costs[dst] if(costs[dst]!=1e9) else -1


