class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if(k==0):
            return False
        seen={}
        for ind,val in enumerate(nums):
            if(val in seen and ind-seen[val]<=k):
                return True
            seen[val]=ind
        return False