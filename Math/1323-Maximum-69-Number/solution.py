class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        i=0
        curr=""
        while i<len(s):
            if(s[i]=="6"): 
                curr+="9"
                i+=1
                break
            else:
                curr+=s[i]
            i+=1
        return int(curr+s[i:])
        
        
        
        