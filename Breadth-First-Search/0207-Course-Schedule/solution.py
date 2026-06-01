class Solution:
    def canFinish(self, n: int, courses: List[List[int]]) -> bool:
        adj_list=defaultdict(list)
        for u,v in courses:
            adj_list[u].append(v)
        '''State of val
            0=Unvisited
            1=Visiting
            2=Visited '''
        #this saves the state of the node, meaning it tells that the course can be taken or not
        states=[0]*n
        def dfs(node):
            #this is to check cycle in graph or courses
            if(states[node]==1):
                return False
            #this tells that current course can be taken
            elif(states[node]==2):
                return True
            #we mark the current course as visiting and then we go for it's prerequisites course and continue this
            states[node]=1
            for val in adj_list[node]:
                #if it's false, it means that course cannot be taken and it is a cycle
                if(not dfs(val)):
                    return False
            #if we have no cycle, then mark curr course as visited
            states[node]=2
            return True
        #here for each course we check can we take it or not??
        for course_no in range(n):
            #this is to check for cycles
            if(not dfs(course_no)):
                return False
        return True