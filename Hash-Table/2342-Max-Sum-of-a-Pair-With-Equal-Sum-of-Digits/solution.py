class Solution:
    def maximumSum(self, nums: List[int]) -> int:   
        def summing(num):
            s=0
            while num>0:
                s+=num%10
                num//=10
            return s
        h1=defaultdict(int)
        maxi=0
        for n in nums:
            curr=0
            su=summing(n)
            if(su in h1):
                curr=n+h1[su]
            if(n>h1[su]):
                h1[su]=n
            maxi=max(curr,maxi)
        if(maxi==0):
            maxi=-1
        return maxi
