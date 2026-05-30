class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        total_penalty=customers.count("Y")
        min_penalty=total_penalty
        min_hour=0
        curr=0
        for i,val in enumerate(customers):
            if(val=="Y"):
                curr+=1
            hour=i+1
            No=(i+1)-curr
            Yes=total_penalty-curr
            curr_penalty=Yes+No
            if(curr_penalty<min_penalty):
                min_hour=hour
                min_penalty=curr_penalty
        return min_hour
        
