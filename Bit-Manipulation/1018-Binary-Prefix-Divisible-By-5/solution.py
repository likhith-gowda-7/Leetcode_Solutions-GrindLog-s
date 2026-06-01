class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res=[]
        binary_num=0
        for bit in nums:
            binary_num=(binary_num*2)+bit
            res.append(binary_num%5==0)
        return res