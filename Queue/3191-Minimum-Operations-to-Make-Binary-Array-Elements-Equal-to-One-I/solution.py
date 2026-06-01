class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res=0
        c=0
        n=len(nums)
        for i in range(n-2):
            if(nums[i]==0):
                c+=1
                nums[i]^=1
                nums[i+1]^=1
                nums[i+2]^=1
        if(nums[-1]+nums[-2]==2):
            return c
        return -1