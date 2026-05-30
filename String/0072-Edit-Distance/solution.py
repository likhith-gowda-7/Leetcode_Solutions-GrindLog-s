class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1=len(word1)
        n2=len(word2)
        dp=list(range(n2+1))
        for i in range(1,n1+1):
            curr=[0]*(n2+1)
            curr[0]=i
            for j in range(1,n2+1):
                val=0
                if(word1[i-1]==word2[j-1]):
                    val=dp[j-1]
                else:
                    diff=min(dp[j-1],dp[j],curr[j-1])
                    val=diff+1
                curr[j]=val
            dp=curr
        return dp[-1]