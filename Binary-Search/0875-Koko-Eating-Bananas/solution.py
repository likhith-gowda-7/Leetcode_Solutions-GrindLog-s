class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi=max(piles)
        l=1
        r=maxi
        while l<=r:
            k=l+(r-l)//2
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/k)
            if(hours>h):
                l=k+1
            else:
                r=k-1
        return l

            
        