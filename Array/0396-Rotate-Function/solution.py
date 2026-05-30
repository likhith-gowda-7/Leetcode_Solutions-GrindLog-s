class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total=sum(nums)
        rotate_sum=0
        n=len(nums)
        for i in range(1,len(nums)):
            rotate_sum+=nums[i]*i
        res=rotate_sum
        for i in range(n-1,0,-1):
            rotate_sum-=nums[i]*(n-1)
            rem=total-nums[i]
            rotate_sum+=rem
            res=max(res,rotate_sum)
        return res