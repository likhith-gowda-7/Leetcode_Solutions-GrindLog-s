class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        mini=min(nums)
        need=0 if(mini%2==0) else 1
        for val in nums:
            if(val%2!=need and (val-mini)%2!=need):
                return False
        return True