class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        prev_end=0
        meetings.sort()
        for start,end in meetings:
            if(start>prev_end):
                days-=end-start+1
            else:
                days-=max(0,end-prev_end)
            prev_end=max(end,prev_end)
        return days

