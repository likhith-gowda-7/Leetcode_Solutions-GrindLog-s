class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l=1
        r=min(time)*totalTrips
        while l<=r:
            mid=(l+r)//2
            trips=0
            for bus in time:
                trips+=mid//bus
            if(trips>=totalTrips):
                r=mid-1
            else:
                l=mid+1
        return l