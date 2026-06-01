class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l=min(batteries)
        r=sum(batteries)//n
        def possible(time):
            needed_power=time*n
            for power in batteries:
                needed_power-=min(power,time)
            if(needed_power<=0):
                return True
            return False
        while l<=r:
            mid=l+(r-l)//2
            if(possible(mid)):
                l=mid+1
            else:
                r=mid-1
        return r
    
        
            
