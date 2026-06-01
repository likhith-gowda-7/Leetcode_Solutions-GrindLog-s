class Solution:
    def findLHS(self, nums: List[int]) -> int:
        h1=Counter(nums)
        res=0
        for n in h1.keys():
            if(n+1 in h1):
                ch=h1[n]+h1[n+1]
                if(ch>res):
                    res=ch
        return res
        