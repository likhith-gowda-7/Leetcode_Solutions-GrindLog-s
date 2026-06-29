class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        maxi=1
        for val in arr[1:]:
            if(val>maxi):
                maxi+=1
        return maxi