class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        h1=defaultdict(list)
        for idx,val in enumerate(nums):
            h1[val].append(idx)
        nums.sort()
        res=[0]*n
        for i in range(n):
            if(i>0 and nums[i]!=nums[i-1]):
                val=nums[i]
                while h1[val]:
                    idx=h1[val].pop()
                    res[idx]=i
        return res