class Solution:
    def summing(self,num):
        t=0
        while num>0:
            t+=num%10
            num//=10
        return t
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        h1=defaultdict(int)
        for i in range(lowLimit,highLimit+1):
            total=self.summing(i)
            h1[total]+=1
        return max(h1.values())
        