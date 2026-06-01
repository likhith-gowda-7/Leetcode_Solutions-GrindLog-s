class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        #solving using line sweep or known as Difference array
        diff_arr=[0]*(len(nums)+1)
        for left,right in queries:
            diff_arr[left]+=1
            diff_arr[right+1]-=1
        #filling diff array
        #Checking that the array can be made zero?
        for i in range(len(nums)):
            if(i>0):
                diff_arr[i]+=diff_arr[i-1]
            if(nums[i]>diff_arr[i]):
                return False
        return True
