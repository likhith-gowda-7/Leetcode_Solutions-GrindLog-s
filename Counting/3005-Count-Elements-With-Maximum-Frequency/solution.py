class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        h1=Counter(nums)
        maxi=max(h1.values())
        total=0
        for val in h1.values():
            if(val==maxi):
                total+=val
        return total