class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        n1=len(a)
        n2=len(b)
        i=n1-1
        j=n2-1
        res=""
        while i>=0 or j>=0:
            total=carry
            if(i>=0):
                total+=int(a[i])
                i-=1
            if(j>=0):
                total+=int(b[j])
                j-=1
            res=str(total%2)+res
            carry=total//2
        if(carry):
            res="1"+res
        return res
        
                
