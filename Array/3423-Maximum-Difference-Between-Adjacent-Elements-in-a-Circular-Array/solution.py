class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n=len(nums)
        nums.append(nums[0])
        maxi=0
        for i in range(n):
            diff=abs(nums[i]-(nums[i+1]))
            if(diff>maxi):
                maxi=diff
        return maxi