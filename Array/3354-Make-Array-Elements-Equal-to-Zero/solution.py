class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        def process(d,idx):
            numbers=nums.copy()
            while 0<=idx<n:
                if(numbers[idx]==0):
                    idx+=d
                else:
                    numbers[idx]-=1
                    #toggling
                    d*=-1
                    idx+=d
            if(max(numbers)==0):
                nonlocal res
                res+=1
        for i,val in enumerate(nums):
            if(val==0):
                process(-1,i-1)
                process(1,i+1)
        return res