class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l=len(nums)
        nums=nums+nums
        stack=[]
        res=[-1]*l
        for i,val in enumerate(nums):
            while stack and nums[stack[-1]]<val:
                ind=stack.pop()
                if(ind<l):
                    res[ind]=val
            stack.append(i)
        return res
        
        

                
            

        
            