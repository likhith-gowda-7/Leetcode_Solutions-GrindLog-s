class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res=0
        for num in nums:
            diff=num%3
            if(diff):
                nearest_num=num//3
                #no of choices
                min_op=min(3-diff,diff-0)
                res+=min_op
        return res