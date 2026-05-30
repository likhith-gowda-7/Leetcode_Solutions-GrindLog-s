class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        zero_count=0
        one_count=0
        res=0
        l=0
        for r in range(len(s)):
            if(s[r]=="1"):
                one_count+=1
            else:
                zero_count+=1
            while one_count>k and zero_count>k:
                if(s[l]=="1"):
                    one_count-=1
                else:
                    zero_count-=1
                l+=1
            res+=r-l+1
        return res

        