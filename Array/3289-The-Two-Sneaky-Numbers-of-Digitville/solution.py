class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        count=[0]*n
        res=[]
        for num in nums:
            count[num]+=1
            if(count[num]==2):
                res.append(num)
        return res