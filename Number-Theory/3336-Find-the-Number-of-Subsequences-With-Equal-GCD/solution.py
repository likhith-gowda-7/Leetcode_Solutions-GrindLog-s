class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod=pow(10,9)+7
        n=len(nums)
        @cache
        def solve(i,g1,g2):
            if(i>=n):
                return 1 if(g1!=0 and g1==g2) else 0
            #Skip
            ans=solve(i+1,g1,g2)
            #taking the element to group 1
            num1=nums[i] if(g1==0) else gcd(g1,nums[i])
            ans+=solve(i+1,num1,g2)
            #taking the element to group 2
            num2=nums[i] if(g2==0) else gcd(g2,nums[i])
            ans+=solve(i+1,g1,num2)
            return ans%mod
        return solve(0,0,0)


