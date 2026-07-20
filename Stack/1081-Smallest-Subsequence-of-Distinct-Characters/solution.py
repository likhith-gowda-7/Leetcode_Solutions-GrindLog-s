class Solution:
    def smallestSubsequence(self, s: str) -> str:
        h1=Counter(s)
        seen=set()
        stack=[]
        for val in s:
            h1[val]-=1
            if(val not in seen):
                while stack and (val<stack[-1] and h1[stack[-1]]>=1):
                    curr=stack.pop()
                    seen.remove(curr)
                stack.append(val)
                seen.add(val)
        return "".join(stack)