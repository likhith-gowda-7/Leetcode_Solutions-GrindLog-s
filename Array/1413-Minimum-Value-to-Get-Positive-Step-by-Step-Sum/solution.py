class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum=0
        curr=0
        for num in nums:
            curr+=num
            min_sum=min(min_sum,curr)
        return 1-(min_sum)
        