class Solution:
    def maxDepth(self, s: str) -> int:
        curr=0
        res=0
        for val in s:
            if(val=="("):
                curr+=1
            elif(val==")"):
                res=max(curr,res)
                curr-=1
        return res