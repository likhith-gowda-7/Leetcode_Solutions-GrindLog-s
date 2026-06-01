class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        occur=Counter(s)
        stack=[]
        seen=set()
        for i in range(len(s)):
            occur[s[i]]-=1
            if(s[i] not in seen):
                while stack and stack[-1]>s[i] and occur[stack[-1]]>0:
                    seen.remove(stack.pop())
                stack.append(s[i])
                seen.add(s[i])
        return "".join(stack)
            

        
        

        
        
        