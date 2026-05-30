class Solution:
    def shortestCommonSupersequence(self, word1: str, word2: str) -> str:
        n1=len(word1)
        n2=len(word2)
        dp=[""]*(n2+1)
        for i in range(1,n1+1):
            curr=[""]*(n2+1)
            for j in range(1,n2+1):
                if(word1[i-1]==word2[j-1]):
                    curr[j]=dp[j-1]+word1[i-1]
                else:
                    val=""
                    if(len(dp[j])>len(curr[j-1])):
                        val=dp[j]
                    else:
                        val=curr[j-1]
                    curr[j]=val
            dp=curr
        common=dp[-1]
        res=[]
        i=0
        j=0
        for ch in common:
            while i<n1 and word1[i]!=ch:
                res.append(word1[i])
                i+=1
            while j<n2 and word2[j]!=ch:
                res.append(word2[j])
                j+=1
            res.append(ch)
            i+=1
            j+=1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)