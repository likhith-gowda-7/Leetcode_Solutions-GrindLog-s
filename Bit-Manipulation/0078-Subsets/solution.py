class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sol=[]
        n=len(nums)
        def backtrack(idx):
            if(idx==n):
                res.append(sol[:])
                return
            #don't pick the number
            backtrack(idx+1)
            #pick the number
            sol.append(nums[idx])
            backtrack(idx+1)
            #undo the changes
            sol.pop()
        backtrack(0)
        return res