class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken=0
        q=deque(tickets)
        while q:
            curr_person=q.popleft()
            time_taken+=1
            if(curr_person>1):
                curr_person-=1
                q.append(curr_person)
            elif(k==0):
                break
            if(k>0):
                k-=1
            else:
                k=len(q)-1
        return time_taken