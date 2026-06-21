class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def check(s1,s2):
            if(len(s1)!=(len(s2)+1)):
                return False
            p1=0
            p2=0
            while p1<len(s1):
                if(p2<len(s2) and s1[p1]==s2[p2]):
                    p1+=1
                    p2+=1
                else:
                    p1+=1
            return (p1==len(s1) and p2==len(s2))
        words.sort(key=lambda x:len(x))
        n=len(words)
        dp=[1]*n
        maxi=1
        for i in range(1,n):
            for prev in range(i):
                if(check(words[i],words[prev]) and (dp[prev]+1)>dp[i]):
                    dp[i]=dp[prev]+1
            if(dp[i]>maxi):
                maxi=dp[i]
        return maxi