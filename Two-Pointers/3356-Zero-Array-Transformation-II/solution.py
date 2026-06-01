class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        diff=[0]*(len(nums)+1)
        sum_val=0
        pos=0
        for i in range(len(nums)):
            while sum_val+diff[i]<nums[i]:
                if(pos==len(queries)):
                    return -1
                st,end,val=queries[pos]
                pos+=1
                if(end<i):
                    continue
                stmax=max(st,i)
                diff[stmax]+=val
                if(end+1<len(nums)):
                    diff[end+1]-=val
            sum_val+=diff[i]
        return pos
                
        

        
