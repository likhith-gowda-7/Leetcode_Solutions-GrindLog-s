class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1=s
        text2=s[::-1]
        n=len(s)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            prev=0
            for j in range(n-1,-1,-1):
                temp=dp[j]
                if(text1[i]==text2[j]):
                    dp[j]=1+prev
                else:
                    dp[j]=max(dp[j],dp[j+1])
                prev=temp
        return dp[0]