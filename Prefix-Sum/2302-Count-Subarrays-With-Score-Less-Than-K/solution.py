class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l=0
        sub_arr=0
        curr=0
        for r in range(len(nums)):
            curr+=nums[r]
            length=r-l+1
            while l<=r and curr*length>=k:
                curr-=nums[l]
                l+=1
                length-=1
            sub_arr+=length
        return sub_arr