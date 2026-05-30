class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        sol=[]
        l=len(candidates)
        def backtrack(idx,curr_sum):
            if(curr_sum==target):
                res.append(sol[:])
                return
            if(idx==l or curr_sum>target):
                return 
            #pick the number(include)
            n=candidates[idx]
            sol.append(n)
            backtrack(idx,curr_sum+n)
            sol.pop()
            #don't pick(skip)
            backtrack(idx+1,curr_sum)       
        backtrack(0,0) 
        return res

