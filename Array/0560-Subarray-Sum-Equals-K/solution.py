class Solution(object):
    def subarraySum(self, nums, k):
        h={0:1}
        count=0
        pr=0
        for num in nums:
            pr+=num
            if(pr-k in h):
                count+=h[pr-k]
            if(pr in h):
                h[pr]+=1
            else:
                h[pr]=1
        return count

            
        
        