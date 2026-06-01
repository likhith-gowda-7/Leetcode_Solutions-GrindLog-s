class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if("b" not in text):
            return 0
        c1=Counter(text)
        c2=Counter("balloon")
        res=float('inf')
        for i in "balloon":
            res=min(res,c1[i]//c2[i])
        return res

        