class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        for i in range(1,len(s)+1):
            res+=(123-ord(s[i-1]))*i
        return res