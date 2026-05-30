class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        st_color=image[sr][sc]
        def check(row,col):
            if(row<0 or row>=m or col<0 or col>=n or image[row][col]!=st_color or image[row][col]==color):
                return False
            return True
        q=deque([(sr,sc)])
        image[sr][sc]=color
        while q:
            row,col=q.popleft()
            for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
                ro=row+r
                co=col+c
                if(check(ro,co)):
                    image[ro][co]=color
                    q.append((ro,co))
        return image