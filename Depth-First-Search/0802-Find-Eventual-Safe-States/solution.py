class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        '''States of a node
        0->Unvisited
        1->Visiting
        2->Visited
        '''
        state=[0]*n
        def dfs(node):
            if state[node] == 1:  # Cycle detected
                return False
            if state[node] == 2:  # Already marked safe
                return True
            
            state[node] = 1  # Mark as visiting
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node] = 2  # Mark as safe
            return True
        safe_nodes=[]
        for node in range(n):
            if(dfs(node)):
                safe_nodes.append(node)
        return safe_nodes