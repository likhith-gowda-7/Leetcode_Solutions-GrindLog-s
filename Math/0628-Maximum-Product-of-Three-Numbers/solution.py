class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1=max2=max3=float('-inf')
        min1=min2=float('inf')
        for val in nums:
            if(val>max1):
                max3=max2
                max2=max1
                max1=val
            elif(val>max2):
                max3=max2
                max2=val
            elif(val>max3):
                max3=val
            if(val<min1):
                min2=min1
                min1=val
            elif(val<min2):
                min2=val
        return max((max1*max2*max3),(max1*min1*min2))