class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Two Phase appoarch
        m=len(heights)
        n=len(heights[0])
        #for pacific ocean
        pacific_nodes=deque()
        pacific_seen=set()
        #for Atlantic ocean
        atlantic_nodes=deque()
        atlantic_seen=set()
        #Add the edges of the two oceans 
        for row in range(m):
            #Left side of the grid(Pacific Ocean)
            pacific_nodes.append((row,0))
            pacific_seen.add((row,0))
            #Right side of the grid(Atlantic Ocean)
            atlantic_nodes.append((row,n-1))
            atlantic_seen.add((row,n-1))
        for col in range(n):
            #Top side of the grid(Pacific Ocean)
            pacific_nodes.append((0,col))
            pacific_seen.add((0,col))
            #Bottom side of the grid(Atlantic Ocean)
            atlantic_nodes.append((m-1,col))
            atlantic_seen.add((m-1,col))
        #Validation of a node
        def check(Row,Col,seen):
            if(Row<0 or Row==m or Col<0 or Col==n or (Row,Col) in seen):
                return False
            return True
        #Detecting all nodes that can reach certain ocean(pacific or atlantic)
        def get_coordinates(q,seen):
            while q:
                row,col=q.popleft()
                #Current cell's height
                curr_h=heights[row][col]
                for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
                    ro=row+r
                    co=col+c
                    if(check(ro,co,seen) and heights[ro][co]>=curr_h):
                        q.append((ro,co))
                        seen.add((ro,co))
        '''After calling this function(get_coordinates),both set's(pacific_seen & atlantic_seen) hold's the nodes that they can reach...'''
        get_coordinates(pacific_nodes,pacific_seen)
        get_coordinates(atlantic_nodes,atlantic_seen)
        #After that, you just have find the common nodes the both set's(pacific_seen & atlantic_seen), to make it simple. we'll use set's intersection operation...
        return list(pacific_seen.intersection(atlantic_seen))



        
