class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod=pow(10,9)+7
        adj_list=defaultdict(list)
        for u,v,time in roads:
            adj_list[u].append((v,time))
            adj_list[v].append((u,time))
        time_needed=[float('inf')]*n
        shortest_time_count=[0]*n
        # heap -> time,node
        heap=[(0,0)]
        time_needed[0]=0
        shortest_time_count[0]=1
        while heap:
            time,node=heappop(heap)
             # Skip outdated distances
            if time > time_needed[node]:
                continue
            for neighbour,t in adj_list[node]:
                curr_time=time+t
                if(curr_time<time_needed[neighbour]):
                    shortest_time_count[neighbour]=shortest_time_count[node]
                    time_needed[neighbour]=curr_time
                    heappush(heap,(curr_time,neighbour))
                elif(curr_time==time_needed[neighbour]):
                    shortest_time_count[neighbour]=(shortest_time_count[neighbour]+shortest_time_count[node])%mod
        return shortest_time_count[n-1]