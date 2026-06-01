class Solution:
    def makeGood(self, s: str) -> str:
        if(len(s)<1):
            return s
        stack=[]
        for i in reversed(s):
            if(stack and stack[-1]!=i and (stack[-1]).lower()==i.lower()):
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack[::-1])