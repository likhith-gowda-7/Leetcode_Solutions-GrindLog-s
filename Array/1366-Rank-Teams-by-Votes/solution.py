class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if(len(votes)==1):
            return votes[0]
        h1=defaultdict(lambda:[0]*len(votes[0]))
        for vote in votes:
            for i in range(len(vote)):
                h1[vote[i]][i]+=1
        return "".join(sorted(h1.keys(),key=lambda x:(h1[x],-ord(x)),reverse=True))