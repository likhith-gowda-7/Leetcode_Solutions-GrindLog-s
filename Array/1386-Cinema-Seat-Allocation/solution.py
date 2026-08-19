class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        def rack():
            return [0]*11
        Seats=defaultdict(rack)
        for row,seat in reservedSeats:
            Seats[row][seat]=1
        res=2*n
        for row,val in Seats.items():
            rack1=sum(val[2:6])
            rack2=sum(val[4:8])
            rack3=sum(val[6:10])
            if((rack1>0 and rack2>0 and rack3>0)):
                res-=2
            elif(rack1!=0 or rack3!=0):
                res-=1
        return res