class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def solve(num):
            total=0
            prod=1
            while num:
                last=num%10
                total+=last
                prod*=last
                num//=10
            return total+prod
        return True if(n%solve(n)==0) else False