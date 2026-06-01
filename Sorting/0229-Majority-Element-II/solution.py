class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if(len(nums)<2):
            return nums
        h1=Counter(nums)
        res=[]
        rule=len(nums)//3
        for key,val in h1.items():
            if(val>rule):
                res.append(key)
        return res
        