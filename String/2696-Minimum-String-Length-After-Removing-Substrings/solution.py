class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        h={"A":"B","C":"D"}
        for i in reversed(s):
            if(stack and i in h and stack[-1]==h[i]):
                stack.pop()
            else:
                stack.append(i)
        return len(stack)

        