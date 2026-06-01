class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n=len(s)
        if(n!=len(goal)):
            return False
        s+=s
        if(goal in s):
            return True
        return False
