class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        mini=min(ranks)
        l=1
        r=mini*(cars**2)
        while l<=r:
            mid=l+(r-l)//2
            s=0
            for rank in ranks:
                s+=int(math.sqrt(mid/rank))
                if(s>=cars):
                    break
            if(s>=cars):
                r=mid-1
            else:
                l=mid+1
        return l
        