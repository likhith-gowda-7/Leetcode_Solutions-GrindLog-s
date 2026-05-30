class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxi=max(candies)
        for i in range(len(candies)):
            if(candies[i]+extraCandies>=maxi):
                candies[i]=True
            else:
                candies[i]=False
        return candies

        