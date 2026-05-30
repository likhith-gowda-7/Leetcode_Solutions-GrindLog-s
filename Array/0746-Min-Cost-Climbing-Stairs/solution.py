class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        prev1,prev2=cost[0],cost[1]
        for i in range(2,n):
            prev1,prev2=prev2,(cost[i]+min(prev1,prev2))
        return min(prev1,prev2)