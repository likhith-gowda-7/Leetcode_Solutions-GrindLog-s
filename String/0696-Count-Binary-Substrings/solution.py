class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr=1
        prev=0
        res=0
        for i in range(1,len(s)):
            if(s[i]!=s[i-1]):
                res+=min(curr,prev)
                prev=curr
                curr=1
            else:
                curr+=1
        res+=min(curr,prev)
        return res