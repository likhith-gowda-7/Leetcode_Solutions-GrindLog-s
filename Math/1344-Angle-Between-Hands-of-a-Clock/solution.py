class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        #It is solved using math formula...
        '''Formula:
            angle=|(30 * hour)-(5.5*minutes)|   '''
        angle=abs((30*hour)-(5.5*minutes))
        return min(angle,360-angle)