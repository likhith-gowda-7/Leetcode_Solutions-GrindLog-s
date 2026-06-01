class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h1={key:val for val,key in enumerate(s)}
        maxi=0
        st=0
        res=[]
        for i in range(len(s)):
            maxi=max(maxi,h1[s[i]])
            if(i==maxi):
                res.append(i-st+1)
                st=i+1
        return res
        