class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod=pow(10,9)+7
        n=len(nums)
        for q in queries:
            l,r,k,v=q
            idx=l
            while idx<=r and idx<n:
                nums[idx]=(nums[idx]*v)%mod
                idx+=k
        res=0
        for val in nums:
            res^=val
        return res