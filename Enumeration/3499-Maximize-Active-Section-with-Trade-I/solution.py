class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n=len(s)
        prev1=0
        prev2=0
        zero_count=0
        res=0
        one_count=0
        for val in s:
            if(val=="0"):
                prev2+=1
            else:
                if(prev1>0 and prev2>0):
                    res=max(res,prev1+prev2)
                if(prev2>0):   
                    prev1=prev2
                    prev2=0
                one_count+=1
        
        if(prev1>0 and prev2>0):
            res=max(res,prev1+prev2)
        return res+one_count

        
        