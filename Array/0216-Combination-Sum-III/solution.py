class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if(n>45):
            return []
        res=[]
        sol=[]
        def backtrack(start,curr_sum):
            if(len(sol)==k and curr_sum==n):
                res.append(sol[:])
                return
            if(len(sol)>=k):
                return
            for i in range(start,10):
                if((curr_sum+i)>n):
                    return
                sol.append(i)
                backtrack(i+1,curr_sum+i)
                sol.pop()
        backtrack(1,0)
        return res