class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        #do spliting 
        v1=version1.split(".")
        v2=version2.split(".")
        m=len(v1)
        n=len(v2)
        for i in range(max(m,n)):
            val1=int(v1[i]) if(i<m) else 0
            val2=int(v2[i]) if(i<n) else 0
            if(val1<val2):
                return -1
            elif(val2<val1):
                return 1
        return 0


        