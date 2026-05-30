class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sol=[]
        n=len(nums)
        used=[False]*n
        def backtrack():
            if(len(sol)==n):
                res.append(sol.copy())
                return
            for i in range(n):
                if(not used[i]):
                    used[i]=True
                    sol.append(nums[i])
                    backtrack()
                    #undo the changes
                    sol.pop()
                    used[i]=False
        backtrack()
        return res
