class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res=[0]*n
        stack=[]
        for curr_day,curr_temp in enumerate(temperatures):
            while stack and stack[-1][1]<curr_temp:
                prev_day,prev_days_temp=stack.pop()
                res[prev_day]=curr_day-prev_day
            stack.append((curr_day,curr_temp))
        return res