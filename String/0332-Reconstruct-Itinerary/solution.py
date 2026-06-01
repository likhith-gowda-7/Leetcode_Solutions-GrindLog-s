class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list=defaultdict(list)
        for u,v in tickets:
            heappush(adj_list[u],v)
        res=[]
        def dfs(node):
            while adj_list[node]:
                v=heappop(adj_list[node])
                dfs(v)
            res.append(node)
        dfs("JFK")
        return res[::-1]
