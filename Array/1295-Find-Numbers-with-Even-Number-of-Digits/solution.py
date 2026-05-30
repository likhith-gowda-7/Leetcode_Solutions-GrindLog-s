class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            ch=len(str(i))
            if(ch%2==0):
                ans+=1
        return ans