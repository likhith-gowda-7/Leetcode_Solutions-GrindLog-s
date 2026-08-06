class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        @cache
        def dfs(l,r):
            if(l==r):
                return nums[l]
            return max(
                nums[l]-dfs(l+1,r),nums[r]-dfs(l,r-1)
            )
        return dfs(0,n-1)>=0