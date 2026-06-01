class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        remaining=len(fruits)
        for i,val in enumerate(fruits):
            for j,cap in enumerate(baskets):
                if(cap>=val):
                    baskets[j]=-1
                    remaining-=1
                    break
        return remaining