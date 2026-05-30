class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        h1=defaultdict(int)
        count=0
        for dom in dominoes:
            #converting list to tuple for hashing
            tup=tuple(dom)
            #if same pair exits,add prev pairs to count
            if(tup in h1):
                count+=h1[tup]
            #if reversed pair exits,add its prev pairs to count
            elif(tup[::-1] in h1):
                count+=h1[tup[::-1]]
                #this is for adding the pair for same group
                h1[tup[::-1]]+=1
                continue
            h1[tup]+=1
        return count
        