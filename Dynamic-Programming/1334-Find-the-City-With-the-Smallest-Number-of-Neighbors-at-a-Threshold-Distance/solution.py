class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        #Dijkstra Algo from all nodes
        adj_list=defaultdict(list)
        #adjacency list for nodes
        for u,v,cost in edges:
            adj_list[u].append((v,cost))
            adj_list[v].append((u,cost))
        #distance list of nodes
        distance=[[int(1e9)]*n for _ in range(n)]
        for source in range(n):
            heap=[(0,source)]
            #premark the distance of a starting node(source)
            distance[source][source]=0
            while heap:
                dist,curr_node=heappop(heap)
                #go to nodes every neighbour
                for neighbour,cost in adj_list[curr_node]:
                    #calculate the distance needed to reach this neighbour(from source)
                    curr_dist=dist+cost
                    '''check this dist is less than prevousely known distance and check if current distance is less than distanceThreshold(Limit), if yes update the neighbour distance'''
                    if(curr_dist<distance[source][neighbour] and curr_dist<=distanceThreshold):
                        distance[source][neighbour]=curr_dist
                        heappush(heap,(curr_dist,neighbour))
        # res -> count_of_reachable_nodes, Node(Starting point)
        res=[float('inf'),-1]
        for node in range(n):
            count=0
            for neighbour in range(n):
                if(node!=neighbour and distance[node][neighbour]!=int(1e9)):
                    count+=1
            if(count<=res[0]):
                res[0]=count
                res[1]=node
        return res[1]

