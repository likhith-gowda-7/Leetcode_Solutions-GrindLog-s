class Solution:
    def longestBalanced(self, s: str) -> int:
        n=len(s)
        res=0
        for i in range(n):
            h1={}
            maxi=0
            for j in range(i,n):
                val=s[j]
                h1[val]=h1.get(val,0)+1
                mini=min(h1.values())
                if(h1[val]>maxi):
                    maxi=h1[val]
                if(mini==maxi):
                    res=max(res,(j-i)+1)
        return res