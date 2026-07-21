class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n=len(s)
        seq=[]
        zero_count=0
        res=0
        one_count=0
        for val in s:
            if(val=="0"):
                zero_count+=1
            else:
                if(zero_count>0):
                    seq.append(zero_count)
                    zero_count=0
                one_count+=1
        if(zero_count>0):
            seq.append(zero_count)
        l=len(seq)
        if(l>1):
            for i in range(1,l):
                curr=seq[i]+seq[i-1]
                res=max(res,curr)
        return res+one_count

        
        