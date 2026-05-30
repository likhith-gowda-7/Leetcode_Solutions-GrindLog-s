class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol=[]
        res=[]
        def backtrack(start):
            if(len(sol)==k):
                res.append(sol[:])
                return
            #this is pruning(for skipping of unneccessary recursion)
            still_need=k-len(sol)
            choices=(n-start)+1
            if(choices>=still_need):
                for i in range(start,n+1):
                        sol.append(i)
                        backtrack(i+1)
                        sol.pop()
        backtrack(1)
        return res