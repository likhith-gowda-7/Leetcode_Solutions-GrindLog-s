class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq=defaultdict(int)
        l=0
        res=1
        sub_len=0
        for r in range(len(nums)):
            freq[nums[r]]+=1
            sub_len+=1
            while freq[nums[r]]>k:
                freq[nums[l]]-=1
                l+=1
                sub_len-=1
            if(sub_len>res):
                res=sub_len
        return res