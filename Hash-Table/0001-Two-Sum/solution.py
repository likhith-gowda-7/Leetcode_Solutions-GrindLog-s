class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h1={}
        for i,val in enumerate(nums):
            rem=target-val
            if(rem in h1):
                return [h1[rem],i]
            h1[val]=i
        