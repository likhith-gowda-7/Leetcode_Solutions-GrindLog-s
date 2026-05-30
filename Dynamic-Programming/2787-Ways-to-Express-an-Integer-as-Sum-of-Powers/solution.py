class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod=pow(10,9)+7
        memo={}
        def dp(remaining,curr):
            tup=(remaining,curr)
            #memoziation
            if(tup in memo):
                return memo[tup]
            power=pow(curr,x)
            if(remaining==0):
                return 1
            if(power>remaining):
                return 0
            take=dp((remaining-power),curr+1)
            skip=dp(remaining,curr+1)
            memo[tup]=(take+skip)%mod
            return memo[tup]
        return dp(n,1)