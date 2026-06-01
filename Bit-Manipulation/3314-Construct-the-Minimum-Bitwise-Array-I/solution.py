class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i,val in enumerate(nums):
            if(val==2):
                nums[i]=-1
                continue
            for j in range(32):            
                if(val & (1<<j) == 0):
                    x=val ^ (1<<j-1)
                    nums[i]=x
                    break
        return nums