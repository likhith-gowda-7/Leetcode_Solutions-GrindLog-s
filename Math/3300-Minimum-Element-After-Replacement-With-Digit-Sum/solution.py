class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini=nums[0]
        for num in nums:
            curr=0
            while num:
                last=num%10
                curr+=last
                num//=10
            mini=min(mini,curr)
        return mini
