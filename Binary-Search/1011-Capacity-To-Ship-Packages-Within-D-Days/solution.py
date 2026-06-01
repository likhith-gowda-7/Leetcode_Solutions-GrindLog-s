class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if(days==1):
            return sum(weights)
        def helper(mid,wieghts,days):
            day=1
            ch=0
            for i in weights:
                ch+=i
                if(ch>mid):
                    day+=1
                    ch=i
            return day>days
        l=max(weights)
        r=sum(weights)
        while l<r:
            mid=l+(r-l)//2
            check=helper(mid,weights,days)
            if(check):
                l=mid+1
            else:
                r=mid
        return l
        