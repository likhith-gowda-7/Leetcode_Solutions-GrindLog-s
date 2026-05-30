class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        memo={}
        def dfs(i):
            if(i>=n):
                return 0
            if(i not in memo):
                #Either skip the current house(n+1) or rob it(nums[i]+dfs(i+2)) and go to next
                memo[i]=max(dfs(i+1),nums[i]+dfs(i+2))
            return memo[i]
        return dfs(0)

        