class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        target_element=nums[n//2]
        min_ops=0
        for val in nums:
            min_ops+=abs(val-target_element)
        return min_ops