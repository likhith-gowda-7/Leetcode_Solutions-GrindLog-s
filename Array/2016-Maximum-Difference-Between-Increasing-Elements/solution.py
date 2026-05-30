class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        take=nums[0]
        maxi=-1
        for i in range(len(nums)):
            diff=nums[i]-take
            take=min(take,nums[i])
            maxi=max(maxi,diff)
        return maxi if(maxi) else -1