class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=set(nums)
        maxi=max(nums)
        for i in range(maxi):
            if(i not in nums):
                return i
        return maxi+1




        