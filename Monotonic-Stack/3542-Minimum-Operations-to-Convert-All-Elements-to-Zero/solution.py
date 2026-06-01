class Solution:
    def minOperations(self, nums: List[int]) -> int:
        min_ops=0
        stack=[]
        for num in nums:
            while stack and stack[-1]>=num:
                if(stack[-1]!=num):
                    min_ops+=1
                stack.pop()
            stack.append(num)
        for num in stack:
            if(num!=0):
                min_ops+=1
        return min_ops