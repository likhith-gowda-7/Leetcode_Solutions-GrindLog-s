class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res=[]
        for q in queries:
            for word in dictionary:
                diff=0
                for i in range(len(word)):
                    if(q[i]!=word[i]):
                        diff+=1
                if(diff<3):
                    res.append(q)
                    break
        return res