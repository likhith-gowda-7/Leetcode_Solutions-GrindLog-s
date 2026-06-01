class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit=0
        buy=prices[0]
        for curr in prices[1:]:
            if(curr<buy):
                buy=curr
            elif(curr>(buy+fee)):
                profit+=curr-(buy+fee)
                buy=curr-fee
        return profit