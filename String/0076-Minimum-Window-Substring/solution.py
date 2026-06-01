class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(t==""):
         return ""
        l=0
        h1=Counter(t)
        h2=defaultdict(int)
        res_len=float("inf")
        have=0
        needed=len(h1)
        start=0
        end=0
        for r in range(len(s)):
            h2[s[r]]+=1
            if(s[r] in h1 and h1[s[r]]==h2[s[r]]):
                have+=1
            while have==needed:
                if((r-l+1)<res_len):
                    start=l
                    end=r
                    res_len=r-l+1
                h2[s[l]]-=1
                if(s[l] in h1 and h2[s[l]]<h1[s[l]]):
                    have-=1
                l+=1
        if(res_len==float('inf')):
            return ""
        return s[start:end+1]


        