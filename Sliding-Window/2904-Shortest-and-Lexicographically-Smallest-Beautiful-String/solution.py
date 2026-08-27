class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n=len(s)
        l=0
        c=0
        res=n
        ones=0
        ans=s+"#"
        for r in range(n):
            if(s[r]=="1"):
                ones+=1
            while ones>=k:
                if(c<res or (c==res and s[l:r+1]<ans)):
                    ans=s[l:r+1]
                    res=c
                if(s[l]=="1"):
                    ones-=1
                l+=1
                c-=1
            c+=1
        return ans if(ans[:-1]!=s) else ""
        