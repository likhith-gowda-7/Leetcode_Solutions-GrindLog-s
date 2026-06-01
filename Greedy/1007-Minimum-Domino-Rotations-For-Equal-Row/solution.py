class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(val):
            #to calculate both list's min operations
            top_mini,botm_mini=0,0
            #both lists have same length
            for i in range(len(tops)):
                #if both are not same then its unable to do swap
                if(tops[i]!=val and bottoms[i]!=val):
                    return -1
                #if top is diff,then you know that bottom[i]==val
                elif(tops[i]!=val):
                    top_mini+=1
                #if bottom is diff,then you know that top[i]==val
                elif(bottoms[i]!=val):
                    botm_mini+=1
            #then find min of both operations
            return min(top_mini,botm_mini)
        res=check(tops[0])
        if(res!=-1):
            return res
        return check(bottoms[0])
        
        
 