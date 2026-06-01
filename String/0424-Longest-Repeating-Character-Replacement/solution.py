class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        res=0
        check=defaultdict(int)
        max_freq=0
        for r in range(len(s)):
            check[s[r]]+=1
            max_freq=max(max_freq,check[s[r]])
            if(r-l+1)-max_freq>k:
                check[s[l]]-=1
                l+=1
            if(r-l+1>res):
                res=r-l+1
        return res


        