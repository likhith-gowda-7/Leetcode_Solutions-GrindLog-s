class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n=len(prices)
        res=0
        l=0
        for i in range(1,n):
            diff=prices[i-1]-prices[i]
            if(diff!=1):
                length=(i-l)
                comb=length*(length+1)//2
                res+=comb
                l=i
        length=(n-l)
        comb=length*(length+1)//2
        res+=comb
        return res