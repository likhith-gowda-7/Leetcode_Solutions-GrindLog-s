class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        h={}
        for s in stones:
            if(s in h):
                h[s]+=1
            else:
                h[s]=1
        res=0
        for j in jewels:
            if(j in h):
                res+=h[j]
        return res
        