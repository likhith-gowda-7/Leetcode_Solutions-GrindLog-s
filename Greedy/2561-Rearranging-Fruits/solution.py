class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq=defaultdict(int)
        min_val=float("inf")
        for i,val in enumerate(basket1):
            min_val=min(min_val,val)
            freq[val]+=1
        for i,val in enumerate(basket2):
            min_val=min(min_val,val)
            freq[val]-=1
        #impossible checking
        #if this runs then it's possible to make both equal or similar, so here we find the minimum cost
        swapable_values=[]
        for key,val in freq.items():
            v=abs(val)
            if(v%2):
                return -1
            half=v//2
            l=[key]*half
            swapable_values.extend(l)
        swapable_values.sort()
        mid=len(swapable_values)//2
        min_cost=0
        for i in range(mid):
            min_cost+=min(swapable_values[i],2*min_val)
        return min_cost
