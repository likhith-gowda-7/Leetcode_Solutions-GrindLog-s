class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        #we sort so that we can attend as much as possible in order
        events.sort(key=lambda i:i[0])
        l=len(events)
        count=0
        min_heap=[]
        day=events[0][0]
        i=0
        while min_heap or i<l:
            #creating a min_heap that which all the events can be attended today and picks in early ending one
            while(i<l and events[i][0]==day):
                heapq.heappush(min_heap,events[i][1])
                i+=1
            #if heap is true and it always has early ending at top and so we attended it 
            if(min_heap):
                heapq.heappop(min_heap)
                count+=1
            #timeskip
            day+=1
            #here we'll remove the meeting that has but still exists in min_heap, becoz meetings can be attended
            while min_heap and min_heap[0]<day:
                heapq.heappop(min_heap)
        return count
