class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res=0
        zero_count=0
        #we are appending a random value which is not 0, so to calculate sub_array's of the array's ending with zeros(0's)
        nums.append(7)
        for n in nums:
            if(n!=0):
                zero_count=0
            else:
                zero_count+=1
                res+=zero_count
        return res
