class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=deque([[0,0] for _ in range(3)])
        for i in range(n-1,-1,-1):
            for holding in range(2):
                ans=0
                if(holding):
                    sell=prices[i]+dp[2][0]
                    hold=dp[1][1]
                    ans=max(sell,hold)
                else:
                    buy=-prices[i]+dp[1][1]
                    skip=dp[1][0]
                    ans=max(buy,skip)
                dp[0][holding]=ans
            dp.pop()
            dp.appendleft([0,0])
        return dp[1][0]
                