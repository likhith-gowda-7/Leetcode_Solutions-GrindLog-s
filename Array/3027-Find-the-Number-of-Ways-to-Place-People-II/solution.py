class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n=len(points)
        points.sort(key=lambda x:(x[0],-x[1]))
        count=0
        for i in range(n-1):
            max_y=float('-inf')
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                if(y1 >= y2 > max_y):
                    count+=1
                    max_y=y2
        return count
