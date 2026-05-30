class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        def check(l,r):
            nonlocal total
            while l>=0 and r<n and s[l]==s[r]:
                total+=1
                l-=1
                r+=1
        total=0
        for i in range(n):
            check(i,i)
            check(i,i+1)
        return total