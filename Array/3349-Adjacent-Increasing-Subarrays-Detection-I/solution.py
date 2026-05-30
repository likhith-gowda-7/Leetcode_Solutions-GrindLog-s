class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev_sub=None
        sub_max=float('-inf')
        sub_size=0
        def check(p,idx,s):
            subs=sub_size//k
            if(subs>=2):
                return True
            if(p!=None and s==k):
                back=idx-k
                if(back<=p):
                    return True
            return False
        for i,n in enumerate(nums):
            if(n>sub_max):
                sub_max=n
                sub_size+=1
                if(check(prev_sub,i,sub_size)):
                    return True
            else:
                if(sub_size>=k):
                    prev_sub=i-1
                sub_size=1
                sub_max=n
                if(check(prev_sub,i,sub_size)):
                    return True
        subs=sub_size//k
        if(subs>=2):
            return True
        return False