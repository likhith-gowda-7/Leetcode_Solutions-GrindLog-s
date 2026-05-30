class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=1
        r=n
        while l<=r:
            mid=l+(r-l)//2
            coin_need=mid*(mid+1)//2
            if(coin_need<=n):
                l=mid+1
            else:
                r=mid-1
        return r
        