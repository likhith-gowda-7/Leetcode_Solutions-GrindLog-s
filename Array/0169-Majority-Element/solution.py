class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)//2
        mc=0
        curr=1
        ele=nums[0]
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]):
                curr+=1
            else:
                curr=1
            if(curr>mc):
                mc=curr
                ele=nums[i]
        return ele




        