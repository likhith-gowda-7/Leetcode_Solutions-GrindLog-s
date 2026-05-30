class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        check=set()
        res=[]
        for n in nums:
            if(n in check):
                res.append(n)
            else:
                check.add(n)
        for i in range(1,len(nums)+1):
            if(i not in check):
                res.append(i)
                break
        return res