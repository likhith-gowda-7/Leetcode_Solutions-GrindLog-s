class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x:len(x))
        n=len(words)
        def solve(s1,s2):
            p1=len(s1)
            p2=len(s2)
            if(p1!=(p2+1)):
                return False
            i=0
            j=0
            while i<p1:
                if(j<p2 and s1[i]==s2[j]):
                    i+=1
                    j+=1
                else:
                    i+=1
            return i==p1 and j==p2
        dp=[1]*(n)
        maxi=1
        for i in range(1,n):
            for prev in range(i-1,-1,-1):
                if(solve(words[i],words[prev]) and (dp[prev]+1)>dp[i]):
                    dp[i]=dp[prev]+1
            maxi=max(maxi,dp[i])
        return maxi
        