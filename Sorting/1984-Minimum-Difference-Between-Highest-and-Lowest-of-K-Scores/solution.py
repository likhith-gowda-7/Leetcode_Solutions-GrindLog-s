class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        k-=1
        mini=float('inf')
        for i in range(k,len(nums)):
            diff=nums[i]-nums[i-k]
            if(diff<mini):
                mini=diff
        return mini