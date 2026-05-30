class Solution:
    def minInsertions(self, s: str) -> int:
        text1=s
        text2=s[::-1]
        n1=len(text1)
        n2=len(text2)
        dp=[0]*(n2+1)
        for i in range(1,n1+1):
            prev=0
            for j in range(1,n2+1):
                temp=dp[j]
                if(text1[i-1]==text2[j-1]):
                    dp[j]=1+prev
                else:
                    dp[j]=max(temp,dp[j-1])
                prev=temp
        return n1-dp[-1]