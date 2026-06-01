class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        #Bottom-Up Solution
        dp=energy.copy()
        n=len(energy)
        for i in range((n-k)-1,-1,-1):
            if((i+k)<n):
                dp[i]+=dp[i+k]
        return max(dp)