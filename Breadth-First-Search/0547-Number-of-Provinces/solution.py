class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V=len(isConnected)
        visited=[0]*V
        def dfs(node):
            if(visited[node]):
                return False
            visited[node]=1
            for v in range(V):
                if(v!=node and isConnected[node][v]):
                    dfs(v)
            return True
        total=0
        for node in range(V):
            if(dfs(node)):
                total+=1
        return total
            