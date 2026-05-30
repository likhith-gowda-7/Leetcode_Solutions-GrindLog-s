class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mini=[float("inf"),0]
        for i in range(len(nums)):
            diff=abs(nums[i]-0)
            if(diff<=mini[0]):
                if(diff==mini[0]):
                    mini[1]=max(mini[1],nums[i])
                else:
                    mini=[diff,nums[i]]
        return mini[1]