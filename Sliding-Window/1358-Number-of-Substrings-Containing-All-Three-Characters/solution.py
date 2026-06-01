class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        size=len(s)
        l=0
        h=defaultdict(int)
        res=0
        for r in range(size):
            h[s[r]]+=1
            while len(h)==3:
                res+=(size-r)
                h[s[l]]-=1
                if(h[s[l]]==0):
                    del h[s[l]]
                l+=1
        return res
        