class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list=defaultdict(list)
        for u,v in prerequisites:
            #to complete u go for v
            adj_list[u].append(v)
        order=[]
        '''
        0->Unvisited
        1->Visiting
        2->Visited
        '''
        state=[0]*n
        def dfs(node):
            if(state[node]==1):
                return False
            if(state[node]==2):
                return True
            #mark visiting
            state[node]=1
            for v in adj_list[node]:
                if(not dfs(v)):
                    return False
            order.append(node)
            state[node]=2
            return True
        for node in range(n):
            if(not dfs(node)):
                return []
        return order


