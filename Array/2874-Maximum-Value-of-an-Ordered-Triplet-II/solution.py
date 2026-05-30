class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val=0
        max_diff=0
        max_trip=0
        for i in nums:
            max_trip=max(max_trip,max_diff*i)
            max_val=max(max_val,i)
            max_diff=max(max_diff,max_val-i)
        return max_trip
        