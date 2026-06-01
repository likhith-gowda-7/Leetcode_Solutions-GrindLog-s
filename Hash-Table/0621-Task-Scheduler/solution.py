class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #trick here is to process the most frequent char
        #this tells how many time the specific char has appeared
        h1=Counter(tasks)
        #this q holds the next executable/available task
        q=deque()
        max_heap=[-cnt for cnt in h1.values()]
        heapq.heapify(max_heap)
        time=0
        while max_heap or q:
            time+=1
            if(max_heap):
                cnt=heapq.heappop(max_heap)
                cnt+=1
                if(cnt!=0):
                    #q stores freq of char and next available time of that task
                    q.append((cnt,time+n))
            #this tells that task that is in top of q is available to execute 
            if(q and q[0][1]==time):
                freq=q.popleft()[0]
                heapq.heappush(max_heap,freq)
        return time