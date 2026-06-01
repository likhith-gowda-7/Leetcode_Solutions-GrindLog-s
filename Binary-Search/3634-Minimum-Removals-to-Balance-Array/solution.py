class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        l=0
        for r in range(n):
            if nums[r]>nums[l]*k:
                l+=1
        return l