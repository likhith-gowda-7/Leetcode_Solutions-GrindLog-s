class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n=len(intervals)
        idx=0
        res=[]
        while idx<n:
            start=intervals[idx][0]
            end=intervals[idx][1]
            while idx<(n-1) and end>=intervals[idx+1][0]:
                idx+=1
                end=max(end,intervals[idx][1])
            res.append([start,end])
            idx+=1
        return res
