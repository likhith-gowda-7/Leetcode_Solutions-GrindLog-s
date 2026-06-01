class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod=pow(10,9)+7
        coord_points={}
        for x,y in points:
            coord_points[y]=coord_points.get(y,0)+1
        prev=0
        res=0
        for key,val in coord_points.items():
            horizontal_lines=(val*(val-1))//2
            res+=horizontal_lines*prev
            prev+=horizontal_lines
        return res%mod