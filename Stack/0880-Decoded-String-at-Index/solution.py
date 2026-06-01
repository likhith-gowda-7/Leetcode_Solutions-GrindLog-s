class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total=0
        for i in s:
            if(i.isdigit()):
                total*=int(i)
            else:
                total+=1
        for c in reversed(s):
            k%=total
            if(k==0 and c.isalpha()):
                return c
            if(c.isdigit()):
                total//=int(c)
            else:
                total-=1
        
        
