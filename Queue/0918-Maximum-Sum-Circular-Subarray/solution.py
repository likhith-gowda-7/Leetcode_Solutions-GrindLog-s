class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxi=nums[0]
        mini=nums[0]
        curr_max=0
        curr_min=0
        total=0
        for i in nums:
            curr_max=max(i,i+curr_max)
            maxi=max(maxi,curr_max)
            curr_min=min(i,i+curr_min)
            mini=min(mini,curr_min)
            total+=i
        if(maxi<0):
            return maxi
        return max(maxi,total-mini)

        