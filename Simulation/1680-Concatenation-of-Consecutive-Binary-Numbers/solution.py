class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod=pow(10,9)+7
        res=0
        digits=0
        for num in range(1,n+1):
            #this number is a power of 2
            if((num & (num-1))==0):
                digits+=1
            res=((res<<digits)+num)%mod
        return res