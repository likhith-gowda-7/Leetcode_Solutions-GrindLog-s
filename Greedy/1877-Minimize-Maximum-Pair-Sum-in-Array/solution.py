class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        maxi=0
        while l<r:
            pair=nums[l]+nums[r]
            if(pair>maxi):
                maxi=pair
            l+=1
            r-=1
        return maxi