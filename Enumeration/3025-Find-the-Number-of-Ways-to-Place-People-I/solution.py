class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        count=0
        n=len(points)
        points.sort(key=lambda x:(-x[0],x[1]))
        for i in range(n-1):
            max_y=float('inf')
            for j in range(i+1,n):
                if(max_y>points[j][1]>=points[i][1]):
                    count+=1
                    max_y=points[j][1]
        return count



        