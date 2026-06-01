class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total_cost=0
        buyed=0
        for candy in cost:
            if(buyed==2):
                buyed=0
                continue
            total_cost+=candy
            buyed+=1
        return total_cost