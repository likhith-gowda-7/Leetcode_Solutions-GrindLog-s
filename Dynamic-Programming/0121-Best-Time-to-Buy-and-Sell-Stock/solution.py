class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        max_profit=0
        for pro in prices[1:]:
            #for finding lowest buy prices
            if(pro<buy):
                buy=pro
            curr=pro-buy
            if(curr>max_profit):
                max_profit=curr
        return max_profit


        