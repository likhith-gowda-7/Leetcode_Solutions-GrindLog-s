class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def bit_or(arr):
            target=0
            for n in arr:
                target|=n
            return target
        t=bit_or(nums)
        count=0
        n=len(nums)
        def backtrack(idx,curr_or):
            if(idx==n):
                nonlocal count
                if(curr_or==t):
                    count+=1
                return
            backtrack(idx+1,curr_or|nums[idx])
            #don't pick it
            backtrack(idx+1,curr_or)
        backtrack(0,0)
        return count