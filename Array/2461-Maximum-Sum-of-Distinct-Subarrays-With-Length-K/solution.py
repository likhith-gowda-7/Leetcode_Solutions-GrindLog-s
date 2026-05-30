class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        elements=set()
        curr_len=0
        l=0
        res=0
        curr=0
        for r in range(len(nums)):
            curr+=nums[r]
            curr_len+=1
            while nums[r] in elements or curr_len>k:
                curr-=nums[l]
                elements.remove(nums[l])
                l+=1
                curr_len-=1
            elements.add(nums[r])
            if(curr_len==k):
                res=max(res,curr)
        return res