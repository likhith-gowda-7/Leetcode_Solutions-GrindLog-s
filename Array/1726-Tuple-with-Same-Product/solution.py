class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        h1=defaultdict(int)
        i=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                pro=nums[i]*nums[j]
                h1[pro]+=1
        res=0
        for val in h1.values():
            pairs=(val*(val-1)//2)
            res+=pairs*8
        return res
