class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1=len(text1)
        n2=len(text2)
        #Taking the One extra row and column for handling base cases effectively...
        dp=[0]*(n2+1)
        for i in range(n1-1,-1,-1):
            prev=0
            for j in range(n2-1,-1,-1):
                temp=dp[j]
                if(text1[i]==text2[j]):
                    dp[j]=1+prev
                else:
                    dp[j]=max(dp[j],dp[j+1])
                prev=temp
        return dp[0]

        