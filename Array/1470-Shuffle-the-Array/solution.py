class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[0]*len(nums)
        idx=0
        for i in range(0,len(nums),2):
            res[i]=nums[idx]
            idx+=1
        for j in range(1,len(nums),2):
            res[j]=nums[idx]
            idx+=1
        return res
