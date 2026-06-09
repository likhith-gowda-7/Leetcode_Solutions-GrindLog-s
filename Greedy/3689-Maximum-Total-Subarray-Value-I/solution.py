class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        #Be Greedy...
        #Because since the Subarray can overlap and the same Subarray can be chosen multiple times.
        '''So Imagine of taking subarray that consists both the most smallest and the most largest elements(such as max(nums),min(nums)) and we'll pick the same subarray k times'''
        max_element=max(nums)
        min_element=min(nums)
        return (max_element-min_element)*k
