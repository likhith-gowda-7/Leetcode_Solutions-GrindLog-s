class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        mini=0
        for i in range(len(seats)):
            curr=abs(seats[i]-students[i])
            mini+=curr
        return mini

