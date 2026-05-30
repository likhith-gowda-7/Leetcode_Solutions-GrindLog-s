class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            if(len(nums)%(i+1)==0):
                mul=nums[i]*nums[i]
                res+=mul
        return res
        