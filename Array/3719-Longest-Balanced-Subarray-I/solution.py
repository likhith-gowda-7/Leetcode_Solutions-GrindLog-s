class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=0
        for i in range(n):
            even=set()
            odd=set()
            for j in range(i,n):
                val=nums[j]
                if(val%2==0):
                    even.add(val)
                else:
                    odd.add(val)
                if(len(even)==len(odd)):
                    maxi=max(maxi,(j-i)+1)
        return maxi