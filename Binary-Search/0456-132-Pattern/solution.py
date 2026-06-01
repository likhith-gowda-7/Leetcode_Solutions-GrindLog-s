class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        mini=float('-inf')
        for n in reversed(nums):
            if(n<mini):
                return True
            while stack and stack[-1]<n:
                mini=stack.pop()
            stack.append(n)
        return False


