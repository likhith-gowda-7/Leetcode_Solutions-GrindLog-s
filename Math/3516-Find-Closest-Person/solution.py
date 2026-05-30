class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        #steps taken by person1 to reach person3
        time1=abs(z-x)
        time2=abs(y-z)
        if(time1<time2):
            return 1
        elif(time2<time1):
            return 2
        else:
            return 0