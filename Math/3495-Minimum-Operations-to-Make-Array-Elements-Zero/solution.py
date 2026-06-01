class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        power_map={}
        p=1
        prev_l=1
        step=1
        while p<=15:
            r=pow(4,p)
            power_map[(prev_l,r-1)]=step
            prev_l=r
            step+=1
            p+=1
        res=0
        for l,r in queries:
            '''traverse the power_map to identify in which range that this query belong too
            tc= O(15) in worst case(Constant)'''
            ops=0
            for ranges,steps in power_map.items():
                L,R=ranges
                if(L>r):
                    break
                left_range=max(l,L)
                right_range=min(r,R)
                if(left_range>right_range):
                    continue
                else:
                    #calculate the no of elements in the current range
                    total_no=(right_range-left_range)+1
                    #calculate the no of operations needed to make a single no to 0
                    ops+=(total_no*steps)
            res+=math.ceil(ops/2)
        return res