class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_one_idx=None
        for i in range(len(nums)):
            if(nums[i]):
                if(prev_one_idx!=None and (i-prev_one_idx)<=k):
                    return False
                prev_one_idx=i
        return True