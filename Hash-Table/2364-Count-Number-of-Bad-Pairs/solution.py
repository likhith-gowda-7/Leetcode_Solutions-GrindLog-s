class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        h1=defaultdict(int)
        total_pair=len(nums)*(len(nums)-1)//2
        good_pair=0
        for ind,val in enumerate(nums):
            good_pair+=h1[val-ind]
            h1[val-ind]+=1  
        return total_pair-good_pair
        