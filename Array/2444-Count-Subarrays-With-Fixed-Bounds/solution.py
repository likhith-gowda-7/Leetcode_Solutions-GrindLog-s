class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res=0
        bad=-1
        mini=-1
        maxi=-1
        for r in range(len(nums)):
            if(nums[r]>maxK or nums[r]<minK):
                bad=r
            if(nums[r]==maxK):
                maxi=r
            if(nums[r]==minK):
                mini=r
            res+=max(0,min(maxi,mini)-bad)
        return res

            

