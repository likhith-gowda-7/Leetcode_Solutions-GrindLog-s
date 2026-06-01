class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        types=[0,0]
        types[0],types[1]=students.count(0),students.count(1)
        q=deque(students)
        while q:
            curr_student=q.popleft()
            if(curr_student==sandwiches[0]):
                sandwiches.pop(0)
                types[curr_student]-=1
            else:
                q.append(curr_student)
                if(types[sandwiches[0]]==0):
                    break
        return len(q)