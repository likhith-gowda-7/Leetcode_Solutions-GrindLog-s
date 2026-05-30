class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        for i in range(len(s)):
            stack.append(s[i])
            if(len(stack)>=len(part)):
                ch="".join(stack[-len(part):])
                if(ch==part):
                    for i in range(len(part)):
                        stack.pop()
        return "".join(stack)
        

        