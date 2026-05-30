class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*(k+1),[0]*(k+1)]
        for i in range(n-1,-1,-1):
            for holding in range(2):
                for trans in range(k):
                    ans=0
                    if(holding==0):
                        buy=-prices[i]+dp[1][trans]
                        skip=dp[0][trans]
                        ans=max(buy,skip)
                    else:
                        sell=prices[i]+dp[0][trans+1]
                        hold=dp[1][trans]
                        ans=max(sell,hold)
                    dp[holding][trans]=ans
        return dp[0][0]