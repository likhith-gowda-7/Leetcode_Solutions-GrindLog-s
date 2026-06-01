class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        free_times=[]
        prev_end=0
        for i in range(len(startTime)):
            free=startTime[i]-prev_end
            free_times.append(free)
            prev_end=endTime[i]
        free_times.append(eventTime-endTime[-1])
        min_heap=[]
        for i in range(len(free_times)):
            if(len(min_heap)<3):
                heapq.heappush(min_heap,(free_times[i],i))
            else:
                if(free_times[i]>min_heap[0][0]):
                    heapq.heappushpop(min_heap,(free_times[i],i))

        def find_pos(l,i):
            for free_time,ind in min_heap:
                #if we have that much space to shift, then check it if that is adjecent of current meeting
                if(free_time>=l and (ind!=(i+1) and (ind!=i))):
                    return True
            return False
        #if we are not able to change any event then this will be the max free time we can get
        res=0
        for i in range(len(startTime)):
            left_time=free_times[i]
            right_time=free_times[i+1]
            length=endTime[i]-startTime[i]
            time=left_time+right_time
            if(find_pos(length,i)):
                time+=length
            res=max(res,time)
        return res
                
