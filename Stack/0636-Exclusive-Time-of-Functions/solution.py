class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        excl_time=[0]*n
        stack=[]
        prev_time=0
        for log in logs:
            f_id, status, time = log.split(":")
            f_id, time = int(f_id), int(time)
            if(status=="start"):
                if(stack):
                    excl_time[stack[-1]]+=time-prev_time
                prev_time=time
                stack.append(f_id)
            else:
                excl_time[stack.pop()]+=(time-prev_time)+1
                prev_time=time+1
        return excl_time
                