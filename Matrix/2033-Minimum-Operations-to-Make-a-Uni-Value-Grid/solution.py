class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr=[]
        diff=None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr=grid[i][j]
                if(diff is None):
                    diff=curr
                elif(abs(diff-curr)%x!=0):
                    return -1
                arr.append(curr)
        #Find the most optimal number to make equal of...
        arr.sort()
        i=len(arr)//2
        mid=arr[i]
        res=0
        for val in arr:
            if(val!=mid):
                diff=abs(val-mid)
                res+=diff//x
        return res