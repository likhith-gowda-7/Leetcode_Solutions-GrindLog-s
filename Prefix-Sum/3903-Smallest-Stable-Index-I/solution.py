class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        mini=[0]*n
        m=float('inf')
        for i in range(n-1,-1,-1):
            m=min(m,nums[i])
            mini[i]=m
        maxi=0
        for i in range(n):
            maxi=max(nums[i],maxi)
            curr=maxi-mini[i]
            if(curr<=k):
                return i
        return -1