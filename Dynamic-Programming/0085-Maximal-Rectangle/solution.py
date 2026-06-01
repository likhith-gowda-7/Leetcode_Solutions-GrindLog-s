class Solution:
    def l_hist(self, heights: List[int]) -> int:
        n=len(heights)
        max_area=0
        stack=[]
        #Area of Rectangle = width*height
        for idx,curr_height in enumerate(heights):
            reachable_till=idx
            while stack and stack[-1][1]>curr_height:
                i,h=stack.pop()
                curr_area=(idx-i)*h
                max_area=max(max_area,curr_area)
                reachable_till=i
            stack.append((reachable_till,curr_height))
        #now for the left heights from their starting to end positions
        for i,curr_height in stack:
            curr_area=(n-i)*curr_height
            max_area=max(max_area,curr_area)
        return max_area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        prefix=[[0]*m for _ in range(n)]
        maxi=0
        for j in range(m):
            s=0
            for i in range(n):
                if(matrix[i][j]=="1"):
                    s+=1
                else:
                    s=0
                prefix[i][j]=s
        for i in range(n):
            maxi=max(maxi,self.l_hist(prefix[i]))
        return maxi
