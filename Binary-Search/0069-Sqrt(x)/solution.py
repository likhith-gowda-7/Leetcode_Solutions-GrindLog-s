class Solution:
    def mySqrt(self, x: int) -> int:
        if(x==0):
            return x
        l=1
        r=x
        while l<=r:
            mid=l+(r-l)//2
            if(mid*mid>x):
                r=mid-1
            elif(mid*mid<x):
                l=mid+1
            else:
                return mid
        return r
        
        