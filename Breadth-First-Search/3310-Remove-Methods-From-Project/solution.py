class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj_list=defaultdict(list)
        indegree=[0]*n
        for u,v in invocations:
            adj_list[u].append(v)
            indegree[v]+=1
        bad_nodes=set([k])
        q=deque([k])
        while q:
            node=q.popleft()
            for v in adj_list[node]:
                if(v not in bad_nodes):
                    q.append(v)
                    bad_nodes.add(v)
                indegree[v]-=1
        connected=False
        res=[]
        for node in range(n):
            if(node not in bad_nodes):
                res.append(node)
            elif(not connected and indegree[node]>0):
                connected=True
        if(connected):
            res.extend(list(bad_nodes))
        return res


        
