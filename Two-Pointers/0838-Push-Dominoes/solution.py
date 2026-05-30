class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        #make a list of input
        values=list(dominoes)
        q=deque()
        length=0
        for ind,val in enumerate(values):
            #adding the pillars to check their impact
            if(val!="."):
                q.append((val,ind))
            length+=1
        #putting the impact on standing pillars
        while q:
            val,ind=q.popleft()
            if(val=="R"):
                if(ind+1<length and values[ind+1]=="."):
                    if(ind+2<length and values[ind+2]=="L"):
                        q.popleft()
                    else:
                        values[ind+1]="R"
                        q.append(("R",ind+1))
            else:
                if(ind>0 and values[ind-1]=="."):
                    values[ind-1]="L"
                    q.append(("L",ind-1))          
        return "".join(values)

