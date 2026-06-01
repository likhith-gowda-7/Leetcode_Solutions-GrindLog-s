class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        maxi=0
        for i in range(1,len(prices)):
            buy=prices[i-1]
            curr=prices[i]-buy
            if(curr>0):
                maxi+=curr
        return maxi


        