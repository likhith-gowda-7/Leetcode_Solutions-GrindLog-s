class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1=len(s)
        n2=len(t)
        @cache
        def solve(i,j):
            if(j==n2):
                return 1
            elif(i==n1):
                return 0
            take=0
            if(s[i]==t[j]):
                take=solve(i+1,j+1)
            skip=solve(i+1,j)
            return take+skip
        return solve(0,0)