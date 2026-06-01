class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        nice=0
        h1=defaultdict(int)
        for i in range(len(nums)):
            val=nums[i]-int(str(nums[i])[::-1])
            nice+=h1[val]
            h1[val]+=1
        return nice%(10**9+7)

        