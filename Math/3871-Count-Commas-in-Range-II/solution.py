class Solution:
    def countCommas(self, n: int) -> int:
        lower=1000
        comma=1
        res=0
        while lower<=n:
            upper=(lower*1000)-1
            if(upper>n):
                upper=n
            res+=((upper-lower)+1)*comma
            comma+=1
            lower=upper+1
        return res