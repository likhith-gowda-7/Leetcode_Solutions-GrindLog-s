class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod=int(1e9)+7
        dp=[0]*(n+1)
        dp[1]=1
        active_sharers=0
        for day in range(2,n+1):
            if(day-delay)>0:
                active_sharers=(active_sharers+dp[day-delay])%mod
            if day-forget>0:
                active_sharers=(active_sharers-dp[day-forget])%mod
            dp[day]=active_sharers
        total=sum(dp[(n-forget)+1:n+1])%mod
        return total
        
        