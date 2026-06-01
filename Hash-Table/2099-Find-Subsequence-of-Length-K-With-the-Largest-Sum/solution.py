class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr=nums[:]
        arr.sort()
        l=len(nums)
        last=l-k
        h1=Counter(arr[last:])
        res=[]
        for i in range(l):
            if(nums[i] in h1 and h1[nums[i]]>0):
                res.append(nums[i])
                h1[nums[i]]-=1
            if(len(res)==k):
                break
        return res
        


