class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        sol=[]
        n=len(nums)
        def bt(idx,curr_sum):
            if(curr_sum==target):
                res.append(sol[:])
                return
            if(idx==n):
                return
            #include it
            val=nums[idx]
            if(curr_sum+val<=target):
                sol.append(val)
                bt(idx+1,curr_sum+val)
                sol.pop()
            #skip duplicate number and 
                while (idx+1)<n and nums[idx]==nums[idx+1]:
                    idx+=1
                bt(idx+1,curr_sum)
        bt(0,0)
        return res
            