class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1=max2=0
        for val in nums:
            if(val>max1):
                max2=max1
                max1=val-1
            elif(val>max2):
                max2=val-1
        return max1*max2