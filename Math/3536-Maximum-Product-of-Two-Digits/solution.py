class Solution:
    def maxProduct(self, n: int) -> int:
        def solve(num):
            max1=0
            max2=0
            while num:
                last=num%10
                if(last>max1):
                    max2=max1
                    max1=last
                elif(last>max2):
                    max2=last
                num//=10
            return max1*max2
        return solve(n)