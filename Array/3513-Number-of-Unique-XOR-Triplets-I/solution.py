class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        if(n<3):
            return n
        power=2
        while power<=n:
            power=(power<<1)
        return power
        
        