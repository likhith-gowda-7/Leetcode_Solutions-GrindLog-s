class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        h1=defaultdict(int)
        min_idx=float('inf')
        for i,val in enumerate(nums):
            s=str(val)
            int_rev=s[::-1].lstrip("0")
            if(s in h1):
                min_idx=min(min_idx,i-h1[s])
            h1[int_rev]=i
        return min_idx if(min_idx!=float('inf')) else -1
