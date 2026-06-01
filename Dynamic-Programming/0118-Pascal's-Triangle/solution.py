class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def pascal(arr):
            sol=[1]
            for i in range(1,len(arr)):
                sol.append(arr[i]+arr[i-1])
            sol.append(1)
            return sol
        res=[[1]]
        val=res[0]
        for i in range(1,numRows):
            val=pascal(val)
            res.append(val)
        return res
        #Recursive Version
        '''res=[]
        def recur(n):
            if(n==1):
                res.append([1])
                return [1]
            prev=recur(n-1)
            sol=[]
            sol.append(1)
            for i in range(1,len(prev)):
                s=prev[i]+prev[i-1]
                sol.append(s)
            sol.append(1)
            res.append(sol)
            return sol
        recur(numRows)
        return res'''
