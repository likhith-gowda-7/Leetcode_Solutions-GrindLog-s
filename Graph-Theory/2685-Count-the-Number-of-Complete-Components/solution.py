class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list=defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        def dfs(node):
            nonlocal vertices,arcs
            vertices+=1
            arcs+=len(adj_list[node])
            seen[node]=True
            for neighbour in adj_list[node]:
                if(not seen[neighbour]):
                    dfs(neighbour)
        res=0
        seen=[False]*n
        for node in range(n):
            if(not seen[node]):
                vertices=arcs=0
                dfs(node)
                res+= (arcs==vertices*(vertices-1))
        return res

