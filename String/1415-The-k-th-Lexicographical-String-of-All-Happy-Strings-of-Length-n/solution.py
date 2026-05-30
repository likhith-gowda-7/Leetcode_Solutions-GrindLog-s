class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res=[""]
        s="abc"
        sol=["p"]
        self.reach=0
        def backtrack(c):
            if(c==n):
                self.reach+=1
                if(self.reach==k):
                    res.append("".join(sol[1:]))
                return
            for curr in s:
                if(curr==sol[-1]):
                    continue
                sol.append(curr)
                backtrack(c+1)
                sol.pop()
        backtrack(0)
        return res[-1]