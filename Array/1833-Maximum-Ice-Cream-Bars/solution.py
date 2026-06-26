class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxi=max(costs)
        Counting=[0]*(maxi+1)
        for cost in costs:
            Counting[cost]+=1
        taken=0
        for cost in range(min(costs),maxi+1):
            if(coins<cost):
                break
            elif(Counting[cost]):
                can_buy=min(Counting[cost],coins//cost)
                taken+=can_buy
                coins-=can_buy*cost
        return taken