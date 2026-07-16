class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n=len(nums)
        maxi=0
        prefix_gcd=[]
        for i in range(n):
            maxi=max(maxi,nums[i])
            prefix_gcd.append(gcd(maxi,nums[i]))
        prefix_gcd.sort()
        left=0
        right=n-1
        gcd_sum=0
        while left<right:
            curr_gcd=gcd(prefix_gcd[left],prefix_gcd[right])
            gcd_sum+=curr_gcd
            left+=1
            right-=1
        return gcd_sum