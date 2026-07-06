class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n=len(board)
        mod=pow(10,9)+7
        max_score=[-1]*(n+1)
        no_of_ways=[0]*(n+1)
        for row in range(n-1,-1,-1):
            curr_score=[-1]*(n+1)
            curr_ways=[0]*(n+1)
            for col in range(n-1,-1,-1):
                cell=board[row][col]
                val=0
                if(cell=="X"):
                    continue
                elif(cell=="S"):
                    curr_score[col]=0
                    curr_ways[col]=1
                    continue
                elif(cell!="E"):
                    val=int(cell)
                top_scores=max(
                    max_score[col],
                    curr_score[col+1],
                    max_score[col+1]
                )
                if(top_scores==-1):
                    continue
                ways=0
                if(top_scores==max_score[col]):
                    ways+=no_of_ways[col]
                if(top_scores==curr_score[col+1]):
                    ways+=curr_ways[col+1]
                if(top_scores==max_score[col+1]):
                    ways+=no_of_ways[col+1]
                curr_score[col]=top_scores+val
                curr_ways[col]=ways%mod
            max_score=curr_score
            no_of_ways=curr_ways
        res=[0,0]
        if(max_score[0]!=-1):
            res=[max_score[0],no_of_ways[0]]
        return res
