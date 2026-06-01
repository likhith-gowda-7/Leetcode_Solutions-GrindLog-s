class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if(k<=1):
            return 0
        count=0
        start=0
        product=1
        for end in range(len(nums)):
            product*=nums[end]
            while product>=k:
                product//=nums[start]
                start+=1
            count+=end-start+1
        return count

                
        