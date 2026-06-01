class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        maxi=0
        l=len(nums)
        for i in range(l):
            for j in range(i+1,l):
                diff=nums[j]-nums[i]
                if(diff>nums[i]):
                    break
                val=nums[j]^nums[i]
                maxi=max(maxi,val)
        return maxi
        
