class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n=len(nums)
        found=0
        i=0
        while i<n-1 and nums[i]<nums[i+1]:
            i+=1
        if(i==0 or i==n-1):
            return False
        while i<n-1 and nums[i]>nums[i+1]:
            i+=1
        if(i==n-1):
            return False
        while i<n-1 and nums[i]<nums[i+1]:
            i+=1
        if(i==n-1):
            return True
        return False
    

