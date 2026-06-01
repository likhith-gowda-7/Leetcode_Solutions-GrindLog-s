class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol=[]
        res=[]
        n=len(nums)
        def backtrack(idx):
            if(idx==n):
                res.append(sol[:])
                return
            sol.append(nums[idx])
            backtrack(idx+1)
            sol.pop()
            while (idx+1)<n and nums[idx]==nums[idx+1]:
                idx+=1
            backtrack(idx+1)
        backtrack(0)
        return res