class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj_list=defaultdict(list)
        for u,v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
        tin=[0]*n
        low=[float("inf")]*n
        time=0
        visited=[0]*n
        res=[]
        def dfs(node,parent):
            nonlocal time
            visited[node]=1
            tin[node]=time
            low[node]=time
            time+=1
            for neighbour in adj_list[node]:
                if(neighbour==parent):
                    continue
                elif(visited[neighbour]==0):
                    dfs(neighbour,node)
                    low[node]=min(low[node],low[neighbour])
                    if(low[neighbour]>tin[node]):
                        res.append([node,neighbour])
                else:
                    low[node]=min(low[node],low[neighbour])
        dfs(0,-1)
        return res

                



        