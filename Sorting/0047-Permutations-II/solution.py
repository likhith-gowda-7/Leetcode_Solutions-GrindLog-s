class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        sol=[]
        n=len(nums)
        used=[False]*n
        def backtrack():
            if(len(sol)==n):
                res.append(sol.copy())
                return
            for i in range(n):
                #this is to avoid duplicate and (not used[i-1]) tells that this is not path value, it is a starting value
                if(i>0 and nums[i]==nums[i-1] and not used[i-1]):
                    continue
                if(not used[i]):
                    used[i]=True
                    sol.append(nums[i])
                    backtrack()
                    sol.pop()
                    used[i]=False
        backtrack()
        return res