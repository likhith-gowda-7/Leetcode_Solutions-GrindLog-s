class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def check(arr):
            for i in range(1,len(arr)):
                if(nums[i]<nums[i-1]):
                    return False
            return True
        min_sum=0
        min_idx=-1
        min_count=0
        while not check(nums):
            min_sum=float('inf')
            min_idx=-1
            min_count+=1
            for i in range(1,len(nums)):
                curr=nums[i-1]+nums[i]
                if(curr<min_sum):
                    min_sum=curr
                    min_idx=i
            nums[min_idx-1]+=nums[min_idx]
            nums.pop(min_idx)
        return min_count
            
