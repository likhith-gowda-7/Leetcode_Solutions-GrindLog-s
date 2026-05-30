class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def comp(s):
            res=""
            skip=0
            for i in s:
                if(i=="#"):
                    if(res):
                        res=res[:-1]
                else:
                    res+=i
            return res
        return comp(s)==comp(t)

