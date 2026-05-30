class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(0,len(nums),3):
            l=nums[i:i+3]
            diff1=l[2]-l[0]
            if(diff1>k):
                return []
            res.append(l)
        return res
            
            