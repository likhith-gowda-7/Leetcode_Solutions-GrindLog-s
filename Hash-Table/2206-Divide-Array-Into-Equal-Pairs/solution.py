class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        check=set()
        for val in nums:
            if(val in check):
                check.remove(val)
            else:
                check.add(val)
        return len(check)==0
        


        