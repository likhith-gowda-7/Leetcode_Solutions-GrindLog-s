class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n=len(nums)
        memo={}
        def dfs(prev,curr):
            if(prev>=(n-1)):
                return 0
            elif(curr>=n):
                return float('-inf')
            if((prev,curr) not in memo):
                diff=(-target <= nums[curr] - nums[prev] <= target)
                take=float('-inf')
                if(diff):
                    take=1+dfs(curr,curr+1)
                skip=dfs(prev,curr+1)
                memo[(prev,curr)]=max(take,skip)
            return memo[(prev,curr)]
        res=dfs(0,1)
        return res if(res!=float('-inf')) else -1