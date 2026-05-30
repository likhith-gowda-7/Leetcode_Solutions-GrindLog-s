class Solution:
    def countOdds(self, low: int, high: int) -> int:
        left=math.ceil(low/2)
        right=math.ceil(high/2)
        res=abs(left-right)
        if(low%2):
            res+=1
        return res