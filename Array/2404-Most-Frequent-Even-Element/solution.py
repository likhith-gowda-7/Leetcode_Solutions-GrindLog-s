class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c=defaultdict(int)
        for n in nums:
            if(n%2==0):
                c[n]+=1
        if(c):
            h=max(c.values())
            ans=float('inf')
            for key,val in c.items():
                if(val==h):
                    if(key<ans):
                        ans=key
            return ans
        return -1


        