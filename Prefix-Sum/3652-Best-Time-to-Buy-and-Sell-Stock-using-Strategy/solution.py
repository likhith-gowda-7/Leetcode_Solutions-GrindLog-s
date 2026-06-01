class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n=len(prices)
        #creating a prefix sum of profits
        base_profit=[prices[0]*strategy[0]]
        prefix_sum=[prices[0]]
        for i in range(1,n):
            curr_profit=prices[i]*strategy[i]
            base_profit.append(base_profit[i-1]+curr_profit)
            prefix_sum.append(prefix_sum[-1]+prices[i])
        l=0
        half=k//2
        k-=1
        total=base_profit[-1]
        max_profit=total
        for r in range(n):
            if(r>=k):
                # Formula=arr[end]-arr[start-1] to find the sum certain range(start,end)
                sub_profit=base_profit[r]
                if(l>0):
                    sub_profit-=base_profit[l-1]
                sum_of_rest=total-sub_profit
                #find the contribution of first & last element in the subarray
                start=r-half
                curr_profit=prefix_sum[r]-prefix_sum[start]
                curr_profit+=sum_of_rest
                max_profit=max(max_profit,curr_profit)
                l+=1
        return max_profit