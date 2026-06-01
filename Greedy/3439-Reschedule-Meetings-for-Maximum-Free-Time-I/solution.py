class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        free_times=[]
        prev_end=0
        for i in range(len(startTime)):
            free=startTime[i]-prev_end
            free_times.append(free)
            prev_end=endTime[i]
        #appending the free time after last meeting
        free_times.append(eventTime-endTime[-1])
        #we'll find the window of size k+1 with max free time(sliding window)
        window=sum(free_times[:k+1])
        time=window
        l=0
        for r in range(k+1,len(free_times)):
            window+=free_times[r]
            window-=free_times[l]
            time=max(time,window)
            l+=1
        return time

        
        