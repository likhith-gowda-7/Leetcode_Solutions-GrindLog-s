class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total=0
        low=float('inf')
        high=0
        for _,y,l in squares:
            total+=l*l
            low=min(y,low)
            high=max(y+l,high)
        target=total/2.0
        while (high-low>1e-5):
            mid=(low+high)/2
            below=0
            for _,y,l in squares:
                if(mid<=y):
                    continue
                elif(mid>(y+l)):
                    below+=l*l
                else:
                    below+=l*(mid-y)
            if(below<target):
                low=mid
            else:
                high=mid
        return low
