class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=0
        left=0
        right=len(nums)-1
        mod=10**9+7
        while left<=right:
            val=nums[left]+nums[right]
            if(val<=target):
                res+=pow(2,right-left,mod)
                left+=1
            else:
                right-=1
        return res%mod
        