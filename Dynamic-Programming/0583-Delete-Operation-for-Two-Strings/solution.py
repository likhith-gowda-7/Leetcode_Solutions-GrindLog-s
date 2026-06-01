class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1=len(word1)
        n2=len(word2)
        dp=[0]*(n2+1)
        for i in range(1,n1+1):
            curr=[0]*(n2+1)
            for j in range(1,n2+1):
                if(word1[i-1]==word2[j-1]):
                    curr[j]=1+dp[j-1]
                else:
                    curr[j]=max(dp[j],curr[j-1])
            dp=curr
        common=dp[-1]
        return (n1-common)+(n2-common)