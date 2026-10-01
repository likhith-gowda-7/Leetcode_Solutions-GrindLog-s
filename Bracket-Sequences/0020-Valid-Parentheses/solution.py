class Solution:
    def isValid(self, s: str) -> bool:
        h1={
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack=[]
        for val in s:
            if(val not in h1):
                stack.append(val)
            elif(not stack or stack[-1]!=h1[val]):
                return False
            else:
                stack.pop()
        return not stack