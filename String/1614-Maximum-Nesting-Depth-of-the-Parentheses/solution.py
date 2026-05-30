class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        maxi=0
        for i in s:
            curr=0
            if(i=="("):
                stack.append(i)
            elif(i==")"):
                curr=len(stack)
                maxi=max(curr,maxi)
                stack.pop()
        return maxi
    
        
        