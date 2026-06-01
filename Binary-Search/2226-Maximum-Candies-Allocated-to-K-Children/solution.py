class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total=sum(candies)
        if(total<k):
            return 0
        l=1
        r=total//k
        while l<=r:
            mid=l+(r-l)//2
            ch=0
            for val in candies:
                ch+=val//mid
            if(ch>=k):
                l=mid+1
            else:
                r=mid-1
        return r

        