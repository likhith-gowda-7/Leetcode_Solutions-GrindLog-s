class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique=set(nums)
        if(min(unique)<k):
            return -1
        l=len(unique)
        if(k in unique):
            l-=1
        return l
        