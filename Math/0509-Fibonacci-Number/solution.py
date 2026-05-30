class Solution:
    def fib(self, n: int) -> int:
        #Tabulation(Bottom-Up) Solution
        if(n<2):
            return n
        #start from base cases
        a,b=0,1
        for n in range(2,n+1):
            #Space Optimized - two states(n-1,n-2)
            a,b=b,a+b
        return b