class Solution:
    def minimumDeletions(self, s: str) -> int:
        b=0
        min_del=0
        for val in s:
            if(val=="b"):
                b+=1
            else:
                min_del=min(min_del+1,b)
        return min_del
        