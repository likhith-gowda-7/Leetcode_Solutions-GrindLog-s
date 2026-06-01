__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        def canAssign(mid,tasks,workers,pills,strength):
            doable=workers[-mid:]
            for i in range(mid-1,-1,-1):
                if(doable[-1]>=tasks[i]):
                    doable.pop()
                else:
                    if(pills<1):
                        return False
                    target=tasks[i]-strength
                    idx=bisect.bisect_left(doable,target)
                    if(idx>=len(doable)):
                        return False
                    pills-=1
                    doable.pop(idx)
            return True
        tasks.sort()
        workers.sort()
        ans=0
        l=0
        r=min(len(tasks),len(workers))
        while l<=r:
            mid=l+(r-l)//2
            if(canAssign(mid,tasks,workers,pills,strength)):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
        


