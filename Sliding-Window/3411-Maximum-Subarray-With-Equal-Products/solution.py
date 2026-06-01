class Solution:
    def maxLength(self, nums: List[int]) -> int:
        longest=0
        for i in range(len(nums)):
            p=nums[i]
            g=nums[i]
            l=nums[i]
            for j in range(i+1,len(nums)):
                p*=nums[j]
                g=gcd(g,nums[j])
                l=lcm(l,nums[j])
                if(p==(g*l)):
                    longest=max(longest,j-i+1)
        return longest