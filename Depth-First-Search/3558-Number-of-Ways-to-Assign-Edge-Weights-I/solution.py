class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        adj_list=defaultdict(list)
        mod=pow(10,9)+7
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        def dfs(node,prev):
            if(not node):
                return 0
            maxi=0
            for v in adj_list[node]:
                if(v!=prev):
                    maxi=max(maxi,dfs(v,node)+1)
            return maxi
        return pow(2,dfs(1,0)-1,mod)