class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        #For every no of (numExchange) empty_bottle, we'll get new full bottle
        res=numBottles #this is always fixed because you can always drink all the full bottles you already have
        while True:
            #this gives the no of new_bottles we can get using old bottles
            new_bottles=numBottles//numExchange
            #this gives the no of extra empty bottles that were left after exchanging the old bottles
            extra_empty_bottles=numBottles%numExchange
            #we'll add the new full bottles to result
            res+=new_bottles
            #after all that, this holds the no of bottles we currently have...
            numBottles=new_bottles+extra_empty_bottles
            #if we doesn't have enough bottles for exchanging, then that's the end..
            if(numBottles<numExchange):
                break
        return res