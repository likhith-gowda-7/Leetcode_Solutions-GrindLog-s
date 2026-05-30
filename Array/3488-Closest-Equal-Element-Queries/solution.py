class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        h1=defaultdict(list)
        n=len(nums)
        for i,val in enumerate(nums):
            h1[val].append(i)
        #apply binary search
        res=[-1]*len(queries)
        for i,q in enumerate(queries):
            val=nums[q]
            n1=len(h1[val])
            if(n1>1):
                idx=bisect.bisect_left(h1[val],q)
                front=h1[val][(idx+1)%n1]-q
                back=q-h1[val][(idx-1)%n1]
                if(idx==0):
                    back=q+(n-h1[val][-1])
                elif(idx==n1-1):
                    front=(n-q)+h1[val][0]
                res[i]=min(front,back)
        return res
