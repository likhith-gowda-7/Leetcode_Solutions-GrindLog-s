class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums=set(nums)
        curr=1
        while (curr*k) in nums:
            curr+=1
        return curr*k