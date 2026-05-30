class Solution:
    def checkString(self, s: str) -> bool:
        b=0
        for val in s:
            if(val=="b"):
                b+=1
            elif(b>0):
                return False
        return True
    
