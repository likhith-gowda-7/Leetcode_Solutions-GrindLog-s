class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, src: int) -> int:
        #Using Dijkstra Algo(heap based)
        adj_list=defaultdict(list)
        #we create a map, in which consists path u->v(with a time it needed to reach)
        for u,v,cost in times:
            adj_list[u].append((v,cost))
        '''this list holds the time required for every node to recieve the signal
        and this list is 1-based indexed, so ignore the 0th index'''
        time_needed=[1e9]*(n+1)
        #premark the source node with time 0
        time_needed[src]=0
        #here heap holds time and a node(at first it has only starting node(source))
        heap=[(0,src)]
        while heap:
            #heap always gives the shortest distance(time) to reach any specific node from current node
            time,node=heapq.heappop(heap)
            #this avoids unneccesary relaxtion of a node, if we have already found the minimum time
            if(time>time_needed[node]):
                continue
            for neighbour,cost in adj_list[node]:
                #here curr time gives the time required to reach the node's neighboures
                curr_time=cost+time
                #if curr_time is less than previously finded, then we have found a new shortest path for this node
                if(curr_time<time_needed[neighbour]):
                    time_needed[neighbour]=curr_time
                    heapq.heappush(heap,(curr_time,neighbour))
        '''we are doing 1-based indexing in this list, so don't include 0 index and we are finding maximum in the list, becoz we need a time taken to reach every node, not a single node'''
        min_time=max(time_needed[1:])
        return min_time if(min_time!=1e9) else -1

            

        
        