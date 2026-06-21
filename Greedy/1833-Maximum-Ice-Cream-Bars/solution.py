class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        taken=0
        for cost in costs:
            if(coins>=cost):
                taken+=1
                coins-=cost
            else:
                break
        return taken