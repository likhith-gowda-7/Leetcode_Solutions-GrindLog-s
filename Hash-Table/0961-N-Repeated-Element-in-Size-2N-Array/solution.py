class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        ele=set()
        for val in nums:
            if(val in ele):
                return val
            ele.add(val)
        