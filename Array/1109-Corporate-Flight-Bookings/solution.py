class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats=[0]*(n+1)
        for fi,la,s in bookings:
            seats[fi-1]+=s
            seats[la]-=s
        for i in range(1,len(seats)):
            seats[i]+=seats[i-1]
        return seats[:-1]
        