class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        l=nsmallest(2,prices)
        ch=money-sum(l)
        if(ch<0):
            ch=money
        return ch
        