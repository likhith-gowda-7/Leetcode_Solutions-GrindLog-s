class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[s[0]]
        for char in s[1:]:
            if stack and stack[-1]==char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
