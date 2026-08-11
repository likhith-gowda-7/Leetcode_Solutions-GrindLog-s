class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seq=nums[0]
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]+1):
                seq+=nums[i]
            else:
                break
        curr=set(nums)
        while seq in curr:
            seq+=1
        return seq