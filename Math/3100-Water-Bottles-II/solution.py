class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res=numBottles #this is always fixed because you can always drink all the full bottles you already have
        while numBottles>=numExchange:
            numBottles-=numExchange   
            res+=1
            numBottles+=1
            numExchange+=1
        return res