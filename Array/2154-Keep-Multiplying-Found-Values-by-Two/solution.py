class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        arr=set(nums)
        while True:
            if(original not in arr):
                break
            original*=2
        return original